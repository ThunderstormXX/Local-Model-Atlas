# SWE-bench Verified

SWE-bench Verified is a human-filtered subset of real software engineering issues.

## What It Measures

Repository understanding, patch generation, and test-passing issue resolution.

## Evaluation

Agents submit patches for 500 verified tasks; the headline score is percent resolved.

Official leaderboard or source: [https://www.swebench.com/](https://www.swebench.com/)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) | leaderboard | swebench_embedded_json |
| [SWE-bench Verified description](https://www.swebench.com/verified.html) | leaderboard | cache_only |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | claude-4-5-opus | no | unknown | 76.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 2 | Gemini 3 Flash Preview | no | unknown | 75.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 3 | minimax-m2.5 | unknown | unknown | 75.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 4 | Claude Opus 4.6 | no | unknown | 75.60% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 5 | claude-opus-4-5-20251101 | no | unknown | 74.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 6 | Gemini 3.1 Pro Preview | no | unknown | 74.20% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 7 | GLM-5 | yes | unknown | 72.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 8 | GPT-5 | no | unknown | 72.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 9 | Claude Sonnet 4.5 | no | unknown | 71.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 10 | Kimi-K2.5 | yes | unknown | 70.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | GLM-5 | yes | unknown | 72.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 2 | Kimi-K2.5 | yes | unknown | 70.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 3 | DeepSeek-V3 | yes | unknown | 70.00% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 4 | [Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | yes | 1000B / A32B | 63.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 5 | devstral-small-2512 | yes | unknown | 56.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 6 | GLM-4.6 | yes | unknown | 55.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 7 | [Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | yes | 480B / A35B | 55.40% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 8 | [GLM-4.5](https://huggingface.co/zai-org/GLM-4.5) | yes | 355B / A32B | 54.20% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 9 | devstral-2512 | yes | unknown | 53.80% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |
| 10 | gpt-oss-120b | yes | 120B | 26.00% | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) |

## Top <=20B Open Models

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

## Best Local Fits

- Best open model fitting a single A100 80GB: [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) - 9.00% (32B, INT4/GGUF estimate)
- Best open model fitting 24GB VRAM: [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) - 9.00% (32B, INT4/GGUF estimate)

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
