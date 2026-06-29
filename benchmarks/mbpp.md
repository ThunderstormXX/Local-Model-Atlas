# MBPP

MBPP evaluates Python program synthesis on short, crowd-sourced programming problems.

## What It Measures

Basic coding ability and unit-test correctness.

## Evaluation

Generated programs are executed against test cases; leaderboards usually report pass@1.

Official leaderboard or source: [https://github.com/google-research/google-research/tree/master/mbpp](https://github.com/google-research/google-research/tree/master/mbpp)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Google Research MBPP repository](https://github.com/google-research/google-research/tree/master/mbpp) | repository | cache_only |
| [EvalPlus leaderboard](https://evalplus.github.io/leaderboard.html) | leaderboard | cache_only |

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
