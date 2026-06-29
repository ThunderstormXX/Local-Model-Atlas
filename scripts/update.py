#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

from local_llm_leaderboard.markdown import write_markdown
from local_llm_leaderboard.models import build_model_index, dedupe_records, enrich_record
from local_llm_leaderboard.normalize import build_alias_map
from local_llm_leaderboard.parsers import PARSERS


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CACHE = DATA / "cache"
GENERATED = DATA / "generated"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def cache_path(url: str) -> Path:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    suffix = Path(url.split("?", 1)[0]).suffix
    if suffix.lower() not in {".csv", ".json", ".html", ".htm", ".txt", ".md", ".js"}:
        suffix = ".html"
    return CACHE / f"{digest}{suffix}"


def fetch_source(url: str, *, refresh: bool, timeout: int) -> tuple[str | None, dict[str, Any]]:
    path = cache_path(url)
    status: dict[str, Any] = {
        "url": url,
        "cache_path": str(path.relative_to(ROOT)),
        "ok": False,
        "bytes": 0,
        "sha256": None,
        "used_cache": False,
        "error": None,
    }

    if not refresh and path.exists():
        text = path.read_text(encoding="utf-8", errors="replace")
        status.update(_content_status(text, used_cache=True))
        return text, status

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Local-Model-Atlas/0.1 (+https://github.com)",
            "Accept": "text/html,application/json,text/csv,text/plain,*/*",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read()
        text = body.decode("utf-8", errors="replace")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        status.update(_content_status(text, used_cache=False))
        return text, status
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        status["error"] = str(exc)
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="replace")
            status.update(_content_status(text, used_cache=True))
            return text, status
        return None, status


def _content_status(text: str, *, used_cache: bool) -> dict[str, Any]:
    encoded = text.encode("utf-8")
    return {
        "ok": True,
        "bytes": len(encoded),
        "sha256": hashlib.sha256(encoded).hexdigest(),
        "used_cache": used_cache,
        "error": None,
    }


def collect_records(
    benchmarks: list[dict[str, Any]],
    *,
    refresh: bool,
    timeout: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    all_records: list[dict[str, Any]] = []
    source_status: list[dict[str, Any]] = []

    for benchmark in benchmarks:
        for source in benchmark.get("sources", []):
            text, status = fetch_source(source["url"], refresh=refresh, timeout=timeout)
            parser_name = source.get("parser", "cache_only")
            parser = PARSERS.get(parser_name)
            status["benchmark"] = benchmark["id"]
            status["source_name"] = source.get("name")
            status["parser"] = parser_name
            status["records"] = 0

            if text is not None and parser is not None:
                try:
                    records = parser(text, benchmark, source)
                    status["records"] = len(records)
                    all_records.extend(records)
                except Exception as exc:  # noqa: BLE001 - source pages are not under our control.
                    status["error"] = f"parse error: {exc}"
            elif parser is None:
                status["error"] = f"unknown parser: {parser_name}"

            source_status.append(status)

    return all_records, source_status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Refresh Local LLM benchmark Markdown.")
    parser.add_argument("--no-fetch", action="store_true", help="Use existing cache files instead of fetching sources.")
    parser.add_argument("--timeout", type=int, default=20, help="Per-source fetch timeout in seconds.")
    args = parser.parse_args(argv)

    benchmarks = load_json(DATA / "benchmarks.json")
    alias_rows = load_json(DATA / "aliases.json")
    model_rows = load_json(DATA / "models.json")
    seed_rows = load_json(DATA / "seed_scores.json")

    CACHE.mkdir(parents=True, exist_ok=True)
    GENERATED.mkdir(parents=True, exist_ok=True)

    fetched_records, source_status = collect_records(
        benchmarks,
        refresh=not args.no_fetch,
        timeout=args.timeout,
    )
    all_raw_records = list(seed_rows) + fetched_records

    alias_map = build_alias_map(alias_rows)
    model_index = build_model_index(model_rows, alias_rows)
    enriched = [enrich_record(record, alias_map, model_index) for record in all_raw_records]
    records = dedupe_records(enriched)
    records.sort(key=lambda row: (row["benchmark"], -float(row["score"]), row["model"]))

    write_json(GENERATED / "records.json", records)
    write_json(GENERATED / "sources.json", source_status)
    write_json(GENERATED / "models.json", model_index)

    write_markdown(ROOT, benchmarks, records, source_status)

    parsed_sources = sum(1 for row in source_status if row.get("records", 0) > 0)
    print(f"Generated {len(records)} normalized rows from {parsed_sources} parseable sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
