# Aider Polyglot

Aider's polyglot benchmark tests code editing across C++, Go, Java, JavaScript, Python, and Rust.

## What It Measures

Code editing accuracy across languages.

## Evaluation

Models edit repositories; the headline score is percent correct.

Official leaderboard or source: [https://aider.chat/docs/leaderboards/](https://aider.chat/docs/leaderboards/)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) | leaderboard | aider_polyglot_html |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | GPT-5 | no | unknown | 88.00% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 2 | o3-pro (high) | no | unknown | 84.90% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 3 | Gemini 2.5 Pro Preview | no | unknown | 83.10% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 4 | o3 (high) | no | unknown | 81.30% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 5 | grok-4 (high) | no | unknown | 79.60% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 6 | o3 (high) + gpt-4.1 | no | unknown | 78.20% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 7 | o3 | no | unknown | 76.90% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 8 | DeepSeek-V3 | yes | unknown | 74.20% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 9 | claude-opus-4-20250514 (32k thinking) | no | unknown | 72.00% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 10 | o4-mini (high) | no | unknown | 72.00% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | DeepSeek-V3 | yes | unknown | 74.20% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 2 | DeepSeek R1 (0528) | yes | unknown | 71.40% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 3 | Qwen3-235B | yes | 235B | 59.60% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 4 | [Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | yes | 1000B / A32B | 59.10% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 5 | DeepSeek R1 | yes | unknown | 56.90% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 6 | [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) | yes | 671B / A37B | 55.10% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 7 | gpt-oss-120b (high) | yes | 120B | 41.80% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 8 | [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | yes | 32B | 40.00% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 9 | QwQ-32B + Qwen 2.5 Coder Instruct | yes | 32B | 26.20% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |
| 10 | qwen-max-2025-01-25 | yes | unknown | 21.80% | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) |

## Top <=20B Open Models

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

## Best Local Fits

- Best open model fitting a single A100 80GB: [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) - 40.00% (32B, INT4/GGUF estimate)
- Best open model fitting 24GB VRAM: [Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) - 40.00% (32B, INT4/GGUF estimate)

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
