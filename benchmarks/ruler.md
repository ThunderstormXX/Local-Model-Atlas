# RULER

RULER evaluates long-context models using configurable synthetic retrieval and reasoning tasks.

## What It Measures

Needle retrieval, variable tracking, aggregation, and long-context robustness.

## Evaluation

Models answer synthetic long-context tasks; reports aggregate accuracy by context length.

Official leaderboard or source: [https://github.com/NVIDIA/RULER](https://github.com/NVIDIA/RULER)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [NVIDIA RULER repository](https://github.com/NVIDIA/RULER) | repository | cache_only |

## Top 10 Overall

_No rows parsed yet._

## Top Open Models

_No rows parsed yet._

## Top <=20B Open Models

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

## Best Local Fits

- Best open model fitting a single A100 80GB: _No matching open-weight model with enough metadata yet._
- Best open model fitting 24GB VRAM: _No matching open-weight model with enough metadata yet._

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
