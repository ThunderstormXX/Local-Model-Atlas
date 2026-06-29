# Berkeley Function Calling Leaderboard

BFCL evaluates tool and function calling across live and non-live tool-use scenarios.

## What It Measures

Function selection, argument construction, relevance, and multi-turn tool use.

## Evaluation

Models produce function calls; official CSVs report aggregate accuracy.

Official leaderboard or source: [https://gorilla.cs.berkeley.edu/leaderboard.html](https://gorilla.cs.berkeley.edu/leaderboard.html)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) | leaderboard | bfcl_csv |
| [BFCL official leaderboard page](https://gorilla.cs.berkeley.edu/leaderboard.html) | leaderboard | cache_only |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | BitAgent-Bounty-8B | yes | 8B | 93.12% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 2 | Gemini 3.1 Pro Preview | no | unknown | 83.12% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 3 | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | yes | 32B | 82.01% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 4 | mistral-large-2411 (FC) | no | unknown | 81.87% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 5 | Claude Sonnet 4.5 | no | unknown | 81.13% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 6 | GLM-4.6 | yes | unknown | 80.90% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 7 | Amazon-Nova-2-Lite-v1:0 (FC) | no | unknown | 80.83% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 8 | Arch-Agent-32B | yes | 32B | 80.68% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 9 | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | yes | 8B | 80.53% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 10 | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | yes | 14B | 80.01% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | BitAgent-Bounty-8B | yes | 8B | 93.12% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 2 | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | yes | 32B | 82.01% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 3 | GLM-4.6 | yes | unknown | 80.90% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 4 | Arch-Agent-32B | yes | 32B | 80.68% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 5 | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | yes | 8B | 80.53% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 6 | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | yes | 14B | 80.01% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 7 | [Mistral-Small-2506](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) | yes | 24B | 79.05% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 8 | [Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | yes | 1000B / A32B | 78.68% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 9 | Qwen3-235B | yes | 235B | 78.68% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |
| 10 | Qwen3-30B | yes | 30B | 78.39% | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) |

## Top <=20B Open Models

| Rank | Model | Params | Context | Score | Gap vs Best Closed | Fits 24GB | Fits 48GB | Fits 80GB |
| ---- | ----- | ------ | ------- | ----- | ------------------ | --------- | --------- | --------- |
| 1 | BitAgent-Bounty-8B | 8B | unknown | 93.12% | +10.00% | yes | yes | yes |
| 2 | [Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8B | 131k | 80.53% | -2.59% | yes | yes | yes |
| 3 | [Qwen3-14B](https://huggingface.co/Qwen/Qwen3-14B) | 14B | 131k | 80.01% | -3.11% | yes | yes | yes |
| 4 | Qwen3-4B | 4B | unknown | 76.39% | -6.73% | yes | yes | yes |
| 5 | Llama-4-Scout-17B-16E-Instruct (FC) | 17B | unknown | 74.69% | -8.43% | yes | yes | yes |
| 6 | Qwen3-1.7B | 1.7B | unknown | 74.61% | -8.51% | yes | yes | yes |
| 7 | [Gemma-3-12B-IT](https://huggingface.co/google/gemma-3-12b-it) | 12B | 128k | 74.24% | -8.88% | yes | yes | yes |
| 8 | Llama-4-Maverick-17B-128E-Instruct-FP8 (FC) | 17B | unknown | 73.65% | -9.47% | yes | yes | yes |
| 9 | Arch-Agent-3B | 3B | unknown | 72.91% | -10.21% | yes | yes | yes |
| 10 | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 8B | 131k | 70.76% | -12.36% | yes | yes | yes |
| 11 | Arch-Agent-1.5B | 1.5B | unknown | 67.73% | -15.39% | yes | yes | yes |
| 12 | Gemma-3-4b-it (Prompt) | 4B | unknown | 60.84% | -22.28% | yes | yes | yes |
| 13 | Llama-3.2-3B-Instruct (FC) | 3B | unknown | 58.33% | -24.79% | yes | yes | yes |
| 14 | Qwen3-0.6B | 0.6B | unknown | 56.62% | -26.50% | yes | yes | yes |
| 15 | Gemma-3-1b-it (Prompt) | 1B | unknown | 11.84% | -71.28% | yes | yes | yes |
| 16 | Llama-3.2-1B-Instruct (FC) | 1B | unknown | 11.77% | -71.35% | yes | yes | yes |

## Best Local Fits

- Best open model fitting a single A100 80GB: BitAgent-Bounty-8B - 93.12% (8B, INT4/GGUF estimate)
- Best open model fitting 24GB VRAM: BitAgent-Bounty-8B - 93.12% (8B, INT4/GGUF estimate)

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
