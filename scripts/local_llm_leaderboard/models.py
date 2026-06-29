from __future__ import annotations

from typing import Any

from .normalize import (
    build_alias_map,
    estimate_vram_gb,
    infer_open_weight,
    infer_organization,
    normalize_model_name,
    param_bucket,
    parse_param_counts,
)


def build_model_index(model_rows: list[dict[str, Any]], alias_rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    alias_map = build_alias_map(alias_rows)
    index: dict[str, dict[str, Any]] = {}
    for row in model_rows:
        canonical = normalize_model_name(row["name"], alias_map)
        merged = dict(row)
        merged["name"] = canonical
        index[canonical] = merged
    return index


def enrich_record(
    record: dict[str, Any],
    alias_map: dict[str, str],
    model_index: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    raw_model = record.get("raw_model") or record.get("model")
    canonical = normalize_model_name(str(raw_model), alias_map)
    enriched = dict(record)
    enriched["model"] = canonical
    enriched["raw_model"] = str(raw_model)

    metadata = dict(model_index.get(canonical, {}))
    for key in (
        "organization",
        "open_weight",
        "architecture",
        "total_params_b",
        "active_params_b",
        "context_length",
        "release_date",
        "huggingface_url",
        "quantization",
    ):
        if key in record and record[key] is not None:
            metadata[key] = record[key]

    total, active = parse_param_counts(canonical)
    if metadata.get("total_params_b") is None and total is not None:
        metadata["total_params_b"] = total
    if metadata.get("active_params_b") is None:
        metadata["active_params_b"] = active if active is not None else metadata.get("total_params_b")

    if metadata.get("organization") is None:
        metadata["organization"] = infer_organization(canonical)
    if metadata.get("open_weight") is None:
        metadata["open_weight"] = infer_open_weight(canonical, metadata.get("organization"))
    if metadata.get("architecture") is None and metadata.get("total_params_b") is not None:
        metadata["architecture"] = "dense"
    if metadata.get("quantization") is None:
        metadata["quantization"] = []

    total_params = metadata.get("total_params_b")
    if total_params is not None:
        total_params = float(total_params)
        metadata["total_params_b"] = total_params
    active_params = metadata.get("active_params_b")
    if active_params is not None:
        metadata["active_params_b"] = float(active_params)

    metadata["param_bucket"] = param_bucket(metadata.get("total_params_b"))
    metadata["vram_gb"] = estimate_vram_gb(metadata.get("total_params_b"))

    enriched.update(metadata)
    return enriched


def dedupe_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best: dict[tuple[str, str], dict[str, Any]] = {}
    aliases: dict[tuple[str, str], set[str]] = {}
    for record in records:
        key = (record["benchmark"], record["model"])
        aliases.setdefault(key, set()).add(record.get("raw_model", record["model"]))
        current = best.get(key)
        if current is None or float(record["score"]) > float(current["score"]):
            best[key] = record
    merged: list[dict[str, Any]] = []
    for key in sorted(best):
        record = dict(best[key])
        record["aliases_seen"] = sorted(aliases.get(key, []))
        merged.append(record)
    return merged


def benchmark_records(records: list[dict[str, Any]], benchmark_id: str) -> list[dict[str, Any]]:
    return sorted(
        [record for record in records if record["benchmark"] == benchmark_id],
        key=lambda row: (-float(row["score"]), row["model"]),
    )


def best_closed(records: list[dict[str, Any]]) -> dict[str, Any] | None:
    closed = [record for record in records if record.get("open_weight") is False]
    if not closed:
        return None
    return max(closed, key=lambda row: float(row["score"]))


def top_open(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [record for record in records if record.get("open_weight") is True]


def small_open(records: list[dict[str, Any]], limit_b: float = 20.0) -> list[dict[str, Any]]:
    return [
        record
        for record in records
        if record.get("open_weight") is True
        and record.get("total_params_b") is not None
        and float(record["total_params_b"]) <= limit_b
    ]
