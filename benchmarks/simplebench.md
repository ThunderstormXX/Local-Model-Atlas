# SimpleBench

SimpleBench targets deceptively simple reasoning problems that are still difficult for frontier models.

## What It Measures

Everyday reasoning, spatial-temporal reasoning, social reasoning, and trick-resistant comprehension.

## Evaluation

Models answer a fixed set of multiple-choice questions; the headline score is accuracy.

Official leaderboard or source: [https://simple-bench.com/](https://simple-bench.com/)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [SimpleBench official site](https://simple-bench.com/) | leaderboard | cache_only |

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
