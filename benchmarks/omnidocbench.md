# OmniDocBench

OmniDocBench evaluates document understanding and parsing across diverse layouts.

## What It Measures

OCR, layout parsing, formula/table understanding, and document reasoning.

## Evaluation

Systems parse and answer over document data; published results use composite metrics.

Official leaderboard or source: [https://github.com/opendatalab/OmniDocBench](https://github.com/opendatalab/OmniDocBench)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [OmniDocBench repository](https://github.com/opendatalab/OmniDocBench) | repository | cache_only |

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
