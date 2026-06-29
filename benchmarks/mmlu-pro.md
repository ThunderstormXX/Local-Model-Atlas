# MMLU-Pro

MMLU-Pro extends MMLU with harder, reasoning-focused questions and more answer choices.

## What It Measures

Robust academic reasoning across 14 domains.

## Evaluation

Models answer multiple-choice questions; the headline score is overall accuracy.

Official leaderboard or source: [https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) | leaderboard | mmlu_pro_csv |
| [TIGER-Lab MMLU-Pro Hugging Face Space](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) | leaderboard | cache_only |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | Gemini 3.1 Pro | no | unknown | 91.16% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 2 | Gemini 3 Pro | no | unknown | 90.10% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 3 | GPT-o1 | no | unknown | 89.30% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 4 | Claude-4.6-Opus(Thinking) | no | unknown | 89.10% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 5 | Gemini 3 Flash | no | unknown | 88.60% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 6 | MiniMax-M2.1 | unknown | 229B | 88.00% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 7 | Qwen3.5-397B | yes | 397B | 87.80% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 8 | Seed2.0-Lite | unknown | unknown | 87.70% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 9 | GPT-5 | no | unknown | 87.50% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 10 | Claude-4.5-Sonnet(Thinking) | no | unknown | 87.40% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | Qwen3.5-397B | yes | 397B | 87.80% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 2 | Qwen3.5-122B | yes | 122B | 86.70% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 3 | Qwen3.5-27B | yes | 27B | 86.10% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 4 | GLM-5 | yes | 754B | 86.00% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 5 | Qwen3-Max-Thinking | yes | unknown | 85.70% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 6 | Qwen3.5-35B | yes | 35B | 85.30% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 7 | DeepSeek-V3 | yes | 685B | 85.00% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 8 | [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) | yes | 355B | 84.60% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 9 | Qwen3-235B | yes | 235B | 84.50% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |
| 10 | DeepSeek-R1 | yes | 671B | 84.00% | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) |

## Top <=20B Open Models

| Rank | Model | Params | Context | Score | Gap vs Best Closed | Fits 24GB | Fits 48GB | Fits 80GB |
| ---- | ----- | ------ | ------- | ----- | ------------------ | --------- | --------- | --------- |
| 1 | Qwen3.5-9B | 9B | unknown | 82.50% | -8.66% | yes | yes | yes |
| 2 | Qwen3.5-4B | 4B | unknown | 79.10% | -12.06% | yes | yes | yes |
| 3 | Phi-4-reasoning-plus | 14B | unknown | 76.00% | -15.16% | yes | yes | yes |
| 4 | Phi-4-reasoning | 14B | unknown | 74.30% | -16.86% | yes | yes | yes |
| 5 | GPT-oss-20B(high) | 20B | unknown | 73.60% | -17.56% | yes | yes | yes |
| 6 | GPT-oss-20B(medium) | 20B | unknown | 73.14% | -18.02% | yes | yes | yes |
| 7 | Phi-4 | 14B | unknown | 70.40% | -20.76% | yes | yes | yes |
| 8 | Qwen2.5-14B | 14B | unknown | 63.69% | -27.47% | yes | yes | yes |
| 9 | [Gemma-3-12B-IT](https://huggingface.co/google/gemma-3-12b-it) | 12B | 128k | 60.60% | -30.56% | yes | yes | yes |
| 10 | NewenAI/Phi4-sft | 14B | unknown | 57.70% | -33.46% | yes | yes | yes |
| 11 | Phi3-medium-4k | 14B | unknown | 55.70% | -35.46% | yes | yes | yes |
| 12 | Qwen3.5-2B | 2B | unknown | 55.30% | -35.86% | yes | yes | yes |
| 13 | Phi-4-mini | 5.6B | unknown | 52.80% | -38.36% | yes | yes | yes |
| 14 | Gemma-2-9B-it | 9B | unknown | 52.08% | -39.08% | yes | yes | yes |
| 15 | Phi3-medium-128k | 14B | unknown | 51.91% | -39.25% | yes | yes | yes |
| 16 | GLM-4 | 9B | unknown | 48.01% | -43.15% | yes | yes | yes |
| 17 | [Phi-3.5-mini-instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct) | 3.8B | 131k | 47.87% | -43.29% | yes | yes | yes |
| 18 | Qwen2-7B | 7B | unknown | 47.24% | -43.92% | yes | yes | yes |
| 19 | Phi3-mini-4k | 3.8B | unknown | 45.66% | -45.50% | yes | yes | yes |
| 20 | Gemma-2-9B | 9B | unknown | 45.10% | -46.06% | yes | yes | yes |
| 21 | Qwen2.5-7B | 7B | unknown | 45.00% | -46.16% | yes | yes | yes |
| 22 | Mistral-Nemo-Instruct-2407 | 12B | unknown | 44.81% | -46.35% | yes | yes | yes |
| 23 | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | 8B | 131k | 44.25% | -46.91% | yes | yes | yes |
| 24 | Phi3-mini-128k | 3.8B | unknown | 43.86% | -47.30% | yes | yes | yes |
| 25 | Qwen2.5-3B | 3B | unknown | 43.73% | -47.43% | yes | yes | yes |
| 26 | Gemma-3-4B-it | 4B | unknown | 43.60% | -47.56% | yes | yes | yes |
| 27 | DeepSeek-Coder-V2-Lite-Instruct | 16B | unknown | 41.57% | -49.59% | yes | yes | yes |
| 28 | [Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 8B | 8k | 40.98% | -50.18% | yes | yes | yes |
| 29 | Mistral-Nemo-Base-2407 | 12B | unknown | 39.77% | -51.39% | yes | yes | yes |
| 30 | Qwen1.5-14B | 14B | unknown | 38.02% | -53.14% | yes | yes | yes |
| 31 | Llama3-Smaug-8B | 8B | unknown | 36.93% | -54.23% | yes | yes | yes |
| 32 | Llama-3-8B | 8B | unknown | 35.36% | -55.80% | yes | yes | yes |
| 33 | DeepseekMath-7B-Instruct | 7B | unknown | 35.30% | -55.86% | yes | yes | yes |
| 34 | DeepSeek-Coder-V2-Lite-Base | 16B | unknown | 34.37% | -56.79% | yes | yes | yes |
| 35 | Gemma-7B | 7B | unknown | 33.73% | -57.43% | yes | yes | yes |
| 36 | Qwen2.5-1.5B | 1.5B | unknown | 32.10% | -59.06% | yes | yes | yes |
| 37 | Mistral-7B-v0.1 | 7B | unknown | 30.88% | -60.28% | yes | yes | yes |
| 38 | [Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) | 7B | 33k | 30.84% | -60.32% | yes | yes | yes |
| 39 | Mistral-7B-v0.2 | 7B | unknown | 30.43% | -60.73% | yes | yes | yes |
| 40 | Qwen3.5-0.8B | 0.8B | unknown | 29.70% | -61.46% | yes | yes | yes |
| 41 | Qwen1.5-7B | 7B | unknown | 29.06% | -62.10% | yes | yes | yes |
| 42 | Mistral-7B-Instruct-v0.1 | 7B | unknown | 25.75% | -65.41% | yes | yes | yes |
| 43 | Llama-2-13B | 13B | unknown | 25.34% | -65.82% | yes | yes | yes |
| 44 | Qwen2-1.5B | 1.5B | unknown | 22.62% | -68.54% | yes | yes | yes |
| 45 | Llama-3.2-3B | 3B | unknown | 22.17% | -68.99% | yes | yes | yes |
| 46 | Llama-2-7B | 7B | unknown | 20.32% | -70.84% | yes | yes | yes |
| 47 | Qwen2-0.5B | 0.5B | unknown | 15.93% | -75.23% | yes | yes | yes |
| 48 | Gemma-2B | 2B | unknown | 15.85% | -75.31% | yes | yes | yes |
| 49 | Gemma-2-2B-it | 2B | unknown | 15.60% | -75.56% | yes | yes | yes |
| 50 | Qwen2.5-0.5B | 0.5B | unknown | 14.92% | -76.24% | yes | yes | yes |
| 51 | Gemma-3-1B-it | 1B | unknown | 14.70% | -76.46% | yes | yes | yes |
| 52 | Llama-3.2-1B | 1B | unknown | 11.95% | -79.21% | yes | yes | yes |

## Best Local Fits

- Best open model fitting a single A100 80GB: Qwen3.5-27B - 86.10% (27B, INT4/GGUF estimate)
- Best open model fitting 24GB VRAM: Qwen3.5-27B - 86.10% (27B, INT4/GGUF estimate)

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
