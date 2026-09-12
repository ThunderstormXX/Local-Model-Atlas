# SWE-bench Verified

SWE-bench Verified is a human-filtered subset of real software engineering issues.

## What It Measures

Repository understanding, patch generation, and test-passing issue resolution.

## Evaluation

Agents submit patches for 500 verified tasks; the headline score is percent resolved.

Official leaderboard or source: [https://www.swebench.com/](https://www.swebench.com/)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) | leaderboard | swebench_embedded_json |
| [SWE-bench Verified description](https://www.swebench.com/verified.html) | leaderboard | cache_only |

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
