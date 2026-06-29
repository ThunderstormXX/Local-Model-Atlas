# SWE-bench Live

SWE-bench Live is an automatically updating SWE-bench-like benchmark for current software tasks.

## What It Measures

Agentic issue resolution on newer, multi-language, multi-OS software tasks.

## Evaluation

Agents submit patches; published results report percent resolved.

Official leaderboard or source: [https://github.com/microsoft/SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Microsoft SWE-bench-Live repository](https://github.com/microsoft/SWE-bench-Live) | repository | cache_only |
| [Live-SWE-agent leaderboard](https://live-swe-agent.github.io/) | leaderboard | cache_only |

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
