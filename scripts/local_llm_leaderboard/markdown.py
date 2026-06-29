from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .models import benchmark_records, best_closed, small_open, top_open
from .normalize import fits_vram


CATEGORY_ORDER = [
    "Coding",
    "Software Engineering",
    "Agent Benchmarks",
    "General reasoning",
    "Tool Use",
    "Long Context",
    "Vision",
]


def markdown_link(label: str, url: str | None) -> str:
    if not url:
        return label
    safe = label.replace("|", "\\|")
    return f"[{safe}]({url})"


def fmt_score(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{float(value):.2f}%"


def fmt_gap(open_score: float | None, closed_score: float | None) -> str:
    if open_score is None or closed_score is None:
        return "n/a"
    return f"{float(open_score) - float(closed_score):+.2f}%"


def fmt_params(record: dict[str, Any]) -> str:
    total = record.get("total_params_b")
    active = record.get("active_params_b")
    if total is None:
        return "unknown"
    if active is not None and float(active) != float(total):
        return f"{float(total):g}B / A{float(active):g}B"
    return f"{float(total):g}B"


def fmt_context(value: Any) -> str:
    if value is None:
        return "unknown"
    try:
        tokens = int(float(value))
    except (TypeError, ValueError):
        return str(value)
    if tokens >= 1000:
        return f"{round(tokens / 1000):g}k"
    return str(tokens)


def fmt_bool(value: bool | None) -> str:
    if value is None:
        return "?"
    return "yes" if value else "no"


def fmt_model(record: dict[str, Any]) -> str:
    return markdown_link(record["model"], record.get("huggingface_url"))


def small_table(records: list[dict[str, Any]], closed: dict[str, Any] | None, limit: int | None = None) -> str:
    rows = small_open(records)
    if limit is not None:
        rows = rows[:limit]
    if not rows:
        return "_No source-attributed open-weight <=20B rows are available from parseable sources yet._\n"
    closed_score = closed["score"] if closed else None
    lines = [
        "| Rank | Model | Params | Context | Score | Gap vs Best Closed | Fits 24GB | Fits 48GB | Fits 80GB |",
        "| ---- | ----- | ------ | ------- | ----- | ------------------ | --------- | --------- | --------- |",
    ]
    for rank, record in enumerate(rows, start=1):
        total = record.get("total_params_b")
        lines.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    fmt_model(record),
                    fmt_params(record),
                    fmt_context(record.get("context_length")),
                    fmt_score(record.get("score")),
                    fmt_gap(record.get("score"), closed_score),
                    fmt_bool(fits_vram(total, 24)),
                    fmt_bool(fits_vram(total, 48)),
                    fmt_bool(fits_vram(total, 80)),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def leaderboard_table(records: list[dict[str, Any]], limit: int = 10) -> str:
    rows = records[:limit]
    if not rows:
        return "_No rows parsed yet._\n"
    lines = [
        "| Rank | Model | Open Weight | Params | Score | Source |",
        "| ---- | ----- | ----------- | ------ | ----- | ------ |",
    ]
    for rank, record in enumerate(rows, start=1):
        source = markdown_link(record.get("source_name") or "source", record.get("source_url"))
        open_weight = record.get("open_weight")
        if open_weight is True:
            open_text = "yes"
        elif open_weight is False:
            open_text = "no"
        else:
            open_text = "unknown"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    fmt_model(record),
                    open_text,
                    fmt_params(record),
                    fmt_score(record.get("score")),
                    source,
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def best_fit_line(records: list[dict[str, Any]], capacity_gb: int) -> str:
    candidates = [
        record
        for record in top_open(records)
        if fits_vram(record.get("total_params_b"), capacity_gb) is True
    ]
    if not candidates:
        return "_No matching open-weight model with enough metadata yet._"
    best = max(candidates, key=lambda row: float(row["score"]))
    return f"{fmt_model(best)} - {fmt_score(best.get('score'))} ({fmt_params(best)}, INT4/GGUF estimate)"


def render_benchmark_page(benchmark: dict[str, Any], all_records: list[dict[str, Any]]) -> str:
    records = benchmark_records(all_records, benchmark["id"])
    closed = best_closed(records)
    open_rows = top_open(records)
    small_rows = small_open(records)

    lines = [
        f"# {benchmark['name']}",
        "",
        benchmark["description"],
        "",
        "## What It Measures",
        "",
        benchmark["measures"],
        "",
        "## Evaluation",
        "",
        benchmark["evaluation"],
        "",
        f"Official leaderboard or source: {markdown_link(benchmark['official_url'], benchmark['official_url'])}",
        "",
        "## Source Coverage",
        "",
        source_table(benchmark),
        "",
        "## Top 10 Overall",
        "",
        leaderboard_table(records, limit=10),
        "## Top Open Models",
        "",
        leaderboard_table(open_rows, limit=10),
        "## Top <=20B Open Models",
        "",
        small_table(small_rows, closed),
        "## Best Local Fits",
        "",
        f"- Best open model fitting a single A100 80GB: {best_fit_line(records, 80)}",
        f"- Best open model fitting 24GB VRAM: {best_fit_line(records, 24)}",
        "",
        "## Notes",
        "",
        "Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.",
        "Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.",
        "",
    ]
    return "\n".join(lines)


def source_table(benchmark: dict[str, Any]) -> str:
    lines = [
        "| Source | Type | Parser |",
        "| ------ | ---- | ------ |",
    ]
    for source in benchmark.get("sources", []):
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_link(source.get("name", "source"), source.get("url")),
                    source.get("kind", "source"),
                    source.get("parser", "cache_only"),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def render_readme(benchmarks: list[dict[str, Any]], records: list[dict[str, Any]]) -> str:
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for benchmark in benchmarks:
        by_category[benchmark["category"]].append(benchmark)

    lines = [
        "# Local LLM Benchmark Tracker",
        "",
        "This repository tracks open-weight LLMs that can realistically be run locally, normalizes model names and parameter counts, and regenerates benchmark Markdown from official sources.",
        "",
        "Run the full update with:",
        "",
        "```bash",
        "python scripts/update.py",
        "```",
        "",
        "Generated tables prioritize official leaderboards and machine-readable assets. Sources that are not yet parseable are still cached and documented on their benchmark page.",
        "",
        "## Benchmark Overview",
        "",
        "| Benchmark | Task | Best Closed | Best <=20B | Gap | Parsed Rows |",
        "| --------- | ---- | ----------- | ---------- | --- | ----------- |",
    ]

    for benchmark in benchmarks:
        rows = benchmark_records(records, benchmark["id"])
        closed = best_closed(rows)
        small = small_open(rows)
        best_small = small[0] if small else None
        closed_text = fmt_model(closed) + " " + fmt_score(closed.get("score")) if closed else "n/a"
        small_text = fmt_model(best_small) + " " + fmt_score(best_small.get("score")) if best_small else "n/a"
        gap = fmt_gap(best_small.get("score"), closed.get("score")) if best_small and closed else "n/a"
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_link(benchmark["name"], f"benchmarks/{benchmark['slug']}.md"),
                    benchmark["task"],
                    closed_text,
                    small_text,
                    gap,
                    str(len(rows)),
                ]
            )
            + " |"
        )

    for category in CATEGORY_ORDER:
        if category not in by_category:
            continue
        lines.extend(["", f"## {category}", ""])
        for benchmark in by_category[category]:
            rows = benchmark_records(records, benchmark["id"])
            closed = best_closed(rows)
            benchmark_href = f"benchmarks/{benchmark['slug']}.md"
            lines.append(f"### {markdown_link(benchmark['name'], benchmark_href)}")
            lines.append("")
            lines.append(small_table(rows, closed, limit=10))

    lines.extend(
        [
            "## Repository Layout",
            "",
            "- `data/benchmarks.json` documents benchmarks and official sources.",
            "- `data/models.json` stores model metadata used for local-fit estimates.",
            "- `data/aliases.json` stores explicit alias merges.",
            "- `data/generated/records.json` stores normalized generated rows.",
            "- `benchmarks/*.md` and this README are generated by `python scripts/update.py`.",
            "",
            "## Automation",
            "",
            "The GitHub Actions workflow in `.github/workflows/update.yml` can run the updater on a schedule and open a pull request when generated tables change.",
            "",
        ]
    )
    return "\n".join(lines)


def render_sources_doc(benchmarks: list[dict[str, Any]], source_status: list[dict[str, Any]]) -> str:
    status_by_url = {row["url"]: row for row in source_status}
    lines = [
        "# Data Sources",
        "",
        "Every benchmark source registered for the updater is listed below. `Records` is the number of score rows parsed from that source during the latest run.",
        "",
        "| Benchmark | Source | Parser | Records | Cache |",
        "| --------- | ------ | ------ | ------- | ----- |",
    ]
    for benchmark in benchmarks:
        for source in benchmark.get("sources", []):
            status = status_by_url.get(source["url"], {})
            cache = status.get("cache_path") or ""
            lines.append(
                "| "
                + " | ".join(
                    [
                        benchmark["name"],
                        markdown_link(source.get("name", "source"), source.get("url")),
                        source.get("parser", "cache_only"),
                        str(status.get("records", 0)),
                        cache,
                    ]
                )
                + " |"
            )
    return "\n".join(lines) + "\n"


def write_markdown(
    root: Path,
    benchmarks: list[dict[str, Any]],
    records: list[dict[str, Any]],
    source_status: list[dict[str, Any]],
) -> None:
    benchmark_dir = root / "benchmarks"
    docs_dir = root / "docs"
    benchmark_dir.mkdir(exist_ok=True)
    docs_dir.mkdir(exist_ok=True)

    (root / "README.md").write_text(render_readme(benchmarks, records), encoding="utf-8")
    for benchmark in benchmarks:
        path = benchmark_dir / f"{benchmark['slug']}.md"
        path.write_text(render_benchmark_page(benchmark, records), encoding="utf-8")
    (docs_dir / "sources.md").write_text(render_sources_doc(benchmarks, source_status), encoding="utf-8")
