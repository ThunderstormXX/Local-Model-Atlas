# MMLU

Massive Multitask Language Understanding evaluates broad subject knowledge across 57 academic and professional domains.

## What It Measures

General knowledge, domain recall, and multiple-choice reasoning.

## Evaluation

Models answer multiple-choice questions; the headline score is accuracy.

Official leaderboard or source: [https://arxiv.org/abs/2009.03300](https://arxiv.org/abs/2009.03300)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [MMLU paper](https://arxiv.org/abs/2009.03300) | paper | cache_only |
| [OpenCompass LLM leaderboard](https://opencompass.org.cn/leaderboard-llm) | leaderboard | cache_only |

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
