# Terminal-Bench

Terminal-Bench evaluates agents on realistic terminal-based tasks.

## What It Measures

Shell use, tool use, debugging, and multi-step task execution.

## Evaluation

Agents work in terminal environments; official leaderboards report task success.

Official leaderboard or source: [https://www.tbench.ai/leaderboard/terminal-bench/2.0](https://www.tbench.ai/leaderboard/terminal-bench/2.0)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Terminal-Bench official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) | leaderboard | cache_only |

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
