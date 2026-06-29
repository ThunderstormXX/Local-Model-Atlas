from __future__ import annotations

import csv
import html
import io
import json
import re
from statistics import mean
from typing import Any, Callable


Record = dict[str, Any]


def parse_percent(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    text = text.replace("%", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return None


def strip_tags(value: str) -> str:
    value = re.sub(r"<script\b[^>]*>.*?</script>", "", value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r"<style\b[^>]*>.*?</style>", "", value, flags=re.IGNORECASE | re.DOTALL)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def base_record(benchmark_id: str, model: str, score: float, source: dict[str, Any]) -> Record:
    return {
        "benchmark": benchmark_id,
        "raw_model": model,
        "score": round(float(score), 4),
        "source_name": source.get("name"),
        "source_url": source.get("url"),
        "source_kind": source.get("kind"),
    }


def parse_cache_only(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    return []


def parse_mmlu_pro_csv(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    rows = csv.DictReader(io.StringIO(text))
    records: list[Record] = []
    for row in rows:
        model = row.get("Models") or row.get("Model")
        score = parse_percent(row.get("Overall"))
        if not model or score is None:
            continue
        # The official CSV stores accuracy as a fraction.
        if score <= 1:
            score *= 100
        record = base_record(benchmark["id"], model, score, source)
        size = parse_percent(row.get("Model Size(B)"))
        if size is not None:
            record["total_params_b"] = size
            record["active_params_b"] = size
        records.append(record)
    return records


def parse_arc_agi_json(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    payload = json.loads(text)
    records: list[Record] = []
    for row in payload.get("evaluations", []):
        model = row.get("modelDisplayName") or row.get("modelId")
        score = row.get("score")
        if model is None or score is None:
            continue
        score_value = float(score)
        if score_value <= 1:
            score_value *= 100
        record = base_record(benchmark["id"], model, score_value, source)
        if row.get("providerDisplayName"):
            record["organization"] = row["providerDisplayName"]
        if row.get("modelReleaseDate"):
            record["release_date"] = str(row["modelReleaseDate"])[:10]
        records.append(record)
    return records


def parse_livecodebench_generation_json(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    payload = json.loads(text)
    by_model: dict[str, list[float]] = {}
    for row in payload.get("performances", []):
        model = row.get("model")
        score = parse_percent(row.get("pass@1"))
        if model and score is not None:
            by_model.setdefault(model, []).append(score)
    records: list[Record] = []
    for model, scores in sorted(by_model.items()):
        if scores:
            record = base_record(benchmark["id"], model, mean(scores), source)
            record["sample_count"] = len(scores)
            records.append(record)
    return records


def parse_bigcodebench_json(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    payload = json.loads(text)
    records: list[Record] = []
    for model, row in payload.items():
        pass_at_1 = row.get("pass@1") or {}
        score = pass_at_1.get("instruct")
        if score is None:
            score = pass_at_1.get("complete")
        score = parse_percent(score)
        if score is None:
            continue
        record = base_record(benchmark["id"], model, score, source)
        if row.get("link"):
            record["huggingface_url"] = row["link"]
        if row.get("size") is not None:
            record["total_params_b"] = float(row["size"])
        if row.get("act_param") is not None:
            record["active_params_b"] = float(row["act_param"])
        if row.get("moe") is not None:
            record["architecture"] = "MoE" if row.get("moe") else "dense"
        if row.get("date"):
            record["release_date"] = row["date"]
        records.append(record)
    return records


def parse_bfcl_csv(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    rows = csv.DictReader(io.StringIO(text))
    records: list[Record] = []
    score_columns = [
        "Live Overall Acc",
        "Non-Live Overall Acc",
        "Multi Turn Overall Acc",
        "Overall Acc",
        "Overall",
    ]
    for row in rows:
        model = row.get("Model")
        score = None
        for col in score_columns:
            score = parse_percent(row.get(col))
            if score is not None:
                break
        if not model or score is None:
            continue
        records.append(base_record(benchmark["id"], model, score, source))
    return records


def parse_swebench_embedded_json(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    match = re.search(
        r'<script[^>]+id=["\']leaderboard-data["\'][^>]*>(?P<json>.*?)</script>',
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not match:
        return []
    payload_text = html.unescape(match.group("json")).strip()
    payload = json.loads(payload_text)
    target = source.get("leaderboard_name", "bash-only")
    leaderboards = [row for row in payload if row.get("name") == target]
    if not leaderboards:
        return []
    records: list[Record] = []
    for row in leaderboards[0].get("results", []):
        if row.get("warning"):
            continue
        model = _swebench_model_name(row)
        score = parse_percent(row.get("resolved"))
        if not model or score is None:
            continue
        record = base_record(benchmark["id"], model, score, source)
        if row.get("oss") is not None:
            record["open_weight"] = bool(row.get("oss"))
        org = _tag_value(row.get("tags") or [], "Org")
        if org:
            record["organization"] = org
        model_size = _tag_value(row.get("tags") or [], "Model_size")
        if model_size:
            size = parse_percent(model_size)
            if size is not None:
                record["total_params_b"] = size
                record["active_params_b"] = size
        if row.get("date"):
            record["release_date"] = row["date"]
        records.append(record)
    return records


def _tag_value(tags: list[str], key: str) -> str | None:
    prefix = f"{key}: "
    for tag in tags:
        if tag.startswith(prefix):
            return tag[len(prefix) :].strip()
    return None


def _swebench_model_name(row: dict[str, Any]) -> str:
    tag_model = _tag_value(row.get("tags") or [], "Model")
    if tag_model:
        return tag_model
    return str(row.get("name") or "").strip()


def parse_aider_polyglot_html(text: str, benchmark: dict[str, Any], source: dict[str, Any]) -> list[Record]:
    records: list[Record] = []
    for match in re.finditer(r'<tr[^>]+id=["\']main-row-\d+["\'][^>]*>(?P<body>.*?)</tr>', text, re.DOTALL):
        cells = re.findall(r"<td\b[^>]*>(.*?)</td>", match.group("body"), flags=re.IGNORECASE | re.DOTALL)
        if len(cells) < 3:
            continue
        model = strip_tags(cells[1])
        score = parse_percent(strip_tags(cells[2]))
        if model and score is not None:
            records.append(base_record(benchmark["id"], model, score, source))
    return records


PARSERS: dict[str, Callable[[str, dict[str, Any], dict[str, Any]], list[Record]]] = {
    "cache_only": parse_cache_only,
    "mmlu_pro_csv": parse_mmlu_pro_csv,
    "arc_agi_json": parse_arc_agi_json,
    "livecodebench_generation_json": parse_livecodebench_generation_json,
    "bigcodebench_json": parse_bigcodebench_json,
    "bfcl_csv": parse_bfcl_csv,
    "swebench_embedded_json": parse_swebench_embedded_json,
    "aider_polyglot_html": parse_aider_polyglot_html,
}
