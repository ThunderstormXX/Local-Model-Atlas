# LiveCodeBench

LiveCodeBench evaluates coding ability on continuously updated programming problems.

## What It Measures

Code generation and problem solving on recent programming tasks.

## Evaluation

Generated solutions are executed against tests; the updater averages official per-problem pass@1 rows.

Official leaderboard or source: [https://livecodebench.github.io/leaderboard.html](https://livecodebench.github.io/leaderboard.html)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) | leaderboard | livecodebench_generation_json |
| [LiveCodeBench leaderboard page](https://livecodebench.github.io/leaderboard.html) | leaderboard | cache_only |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | O4-Mini (High) | no | unknown | 87.30% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 2 | O3 (High) | no | unknown | 84.74% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 3 | O4-Mini (Medium) | no | unknown | 84.45% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 4 | DeepSeek-R1-0528 | yes | unknown | 84.36% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 5 | Gemini 2.5 Pro | no | unknown | 84.27% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 6 | OpenReasoning-Nemotron-32B | unknown | 32B | 80.96% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 7 | EXAONE-4.0-32B | unknown | 32B | 80.88% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 8 | Qwen3-235B | yes | 235B | 80.38% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 9 | XBai-o4-medium | no | unknown | 80.09% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 10 | OpenCodeReasoning-Nemotron-1.1-32B | unknown | 32B | 78.53% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | DeepSeek-R1-0528 | yes | unknown | 84.36% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 2 | Qwen3-235B | yes | 235B | 80.38% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |
| 3 | [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) | yes | 671B / A37B | 49.55% | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) |

## Top <=20B Open Models

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

## Best Local Fits

- Best open model fitting a single A100 80GB: _No matching open-weight model with enough metadata yet._
- Best open model fitting 24GB VRAM: _No matching open-weight model with enough metadata yet._

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
