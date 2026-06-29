# Needle In A Haystack

Needle In A Haystack tests whether a model can retrieve a hidden fact from long contexts.

## What It Measures

Long-context recall and retrieval at different depths and lengths.

## Evaluation

Models answer questions about inserted facts; reports retrieval accuracy over depth and length.

Official leaderboard or source: [https://github.com/gkamradt/LLMTest_NeedleInAHaystack](https://github.com/gkamradt/LLMTest_NeedleInAHaystack)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Needle In A Haystack repository](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | repository | cache_only |

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
