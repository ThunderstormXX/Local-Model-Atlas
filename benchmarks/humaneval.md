# HumanEval

HumanEval evaluates whether models can synthesize Python functions that pass hidden unit tests.

## What It Measures

Code generation correctness on small programming tasks.

## Evaluation

Generated code is executed against tests; leaderboards usually report pass@1.

Official leaderboard or source: [https://github.com/openai/human-eval](https://github.com/openai/human-eval)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [OpenAI HumanEval repository](https://github.com/openai/human-eval) | repository | cache_only |
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
