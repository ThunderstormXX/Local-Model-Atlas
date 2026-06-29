# DocVQA

DocVQA evaluates visual question answering over document images.

## What It Measures

OCR, document layout understanding, and grounded question answering.

## Evaluation

Models answer document questions; official evaluations report ANLS-style scores.

Official leaderboard or source: [https://rrc.cvc.uab.es/?ch=17](https://rrc.cvc.uab.es/?ch=17)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [DocVQA official challenge](https://rrc.cvc.uab.es/?ch=17) | leaderboard | cache_only |

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
