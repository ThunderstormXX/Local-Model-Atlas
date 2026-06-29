# BigCodeBench

BigCodeBench evaluates code generation on practical and library-rich programming tasks.

## What It Measures

Instruction-following code generation and completion quality.

## Evaluation

Generated code is executed against tests; this tracker uses the best available official pass@1 field per model.

Official leaderboard or source: [https://bigcode-bench.github.io/](https://bigcode-bench.github.io/)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) | leaderboard | bigcodebench_json |
| [BigCodeBench hard JSON](https://bigcode-bench.github.io/results-hard.json) | leaderboard | bigcodebench_json |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | [GPT-4o](https://openai.com/index/hello-gpt-4o/) | no | unknown | 51.10% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 2 | [OpenCodeInterpreter-DS-33B](https://huggingface.co/m-a-p/OpenCodeInterpreter-DS-33B) | unknown | 33B | 51.00% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 3 | [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3) | yes | 671B / A37B | 50.00% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 4 | [KwaiCoder-23B-A4B-v1](https://huggingface.co/Kwaipilot/KwaiCoder-23B-A4B-v1) | unknown | 23B / A4B | 49.90% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 5 | [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | yes | 109B / A17B | 49.70% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 6 | [Quasar-Alpha](https://openrouter.ai/openrouter/quasar-alpha) | unknown | unknown | 49.60% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 7 | [Gemini-Exp-1114](https://deepmind.google/technologies/gemini) | no | unknown | 49.20% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 8 | [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | yes | 32B | 49.00% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 9 | [DeepSeek-V2-Chat (2024-06-28)](https://www.deepseek.com/) | yes | 236B / A21B | 48.90% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 10 | [GPT-4.1-Mini-2025-04-14](https://openai.com/index/gpt-4-1/) | no | unknown | 48.90% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |

## Top Open Models

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | [DeepSeek-V3-0324](https://huggingface.co/deepseek-ai/DeepSeek-V3) | yes | 671B / A37B | 50.00% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 2 | [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | yes | 109B / A17B | 49.70% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 3 | [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | yes | 32B | 49.00% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 4 | [DeepSeek-V2-Chat (2024-06-28)](https://www.deepseek.com/) | yes | 236B / A21B | 48.90% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 5 | [DeepSeek-V2.5-1210](deepseek-ai/DeepSeek-V2.5-1210) | yes | 236B / A21B | 48.60% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 6 | [DeepSeek-Coder-V2-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct) | yes | 236B / A21B | 48.20% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 7 | [Qwen2.5-Coder-14B](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | yes | 14B | 48.20% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 8 | [Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | yes | 70B | 46.90% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 9 | [DeepSeek-Coder-33B-Base](https://huggingface.co/deepseek-ai/deepseek-coder-33b-base) | yes | 33B | 46.60% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |
| 10 | [Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) | yes | 70B | 46.10% | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) |

## Top <=20B Open Models

| Rank | Model | Params | Context | Score | Gap vs Best Closed | Fits 24GB | Fits 48GB | Fits 80GB |
| ---- | ----- | ------ | ------- | ----- | ------------------ | --------- | --------- | --------- |
| 1 | [Qwen2.5-Coder-14B](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | 14B | unknown | 48.20% | -2.90% | yes | yes | yes |
| 2 | [Qwen1.5-7B](https://huggingface.co/Qwen/CodeQwen1.5-7B) | 7B | unknown | 45.60% | -5.50% | yes | yes | yes |
| 3 | [Phi-4](https://huggingface.co/microsoft/phi-4) | 14.7B | unknown | 45.50% | -5.60% | yes | yes | yes |
| 4 | [DeepSeek-Coder-6.7B-Base](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-base) | 6.7B | unknown | 41.80% | -9.30% | yes | yes | yes |
| 5 | [Qwen2.5-Coder-7B](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | 7B | unknown | 40.40% | -10.70% | yes | yes | yes |
| 6 | [Qwen2.5-14B](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) | 14B | unknown | 39.80% | -11.30% | yes | yes | yes |
| 7 | [StarCoder2-15B](https://huggingface.co/bigcode/starcoder2-15b) | 15B | unknown | 38.40% | -12.70% | yes | yes | yes |
| 8 | [CodeGemma-7B](https://huggingface.co/google/codegemma-7b) | 7B | unknown | 38.30% | -12.80% | yes | yes | yes |
| 9 | [DeepSeek-R1-Distill-Qwen-14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B) | 14B | 131k | 38.10% | -13.00% | yes | yes | yes |
| 10 | [Phi-3-Medium-128K-Instruct](https://huggingface.co/microsoft/Phi-3-medium-128k-instruct) | 14B | unknown | 37.60% | -13.50% | yes | yes | yes |
| 11 | [Qwen2.5-7B](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) | 7B | unknown | 37.60% | -13.50% | yes | yes | yes |
| 12 | [StarCoder2-15B-Instruct-v0.1](https://huggingface.co/bigcode/starcoder2-15b-instruct-v0.1) | 15B | unknown | 37.60% | -13.50% | yes | yes | yes |
| 13 | [DeepSeek-Coder-V2-Lite-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) | 16B / A2.4B | unknown | 36.80% | -14.30% | yes | yes | yes |
| 14 | [Phi-3.1-Mini-128K-Instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) | 3.8B | unknown | 36.80% | -14.30% | yes | yes | yes |
| 15 | [Magicoder-S-DS-6.7B](https://huggingface.co/ise-uiuc/Magicoder-S-DS-6.7B) | 6.7B | unknown | 36.20% | -14.90% | yes | yes | yes |
| 16 | [DeepSeek-Coder-6.7B-Instruct](https://huggingface.co/deepseek-ai/deepseek-coder-6.7b-instruct) | 6.7B | unknown | 35.50% | -15.60% | yes | yes | yes |
| 17 | [Gemma-2-9B-Instruct](https://huggingface.co/google/gemma-2-9b-it) | 9B | unknown | 34.70% | -16.40% | yes | yes | yes |
| 18 | [Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct) | 8B | 131k | 32.80% | -18.30% | yes | yes | yes |
| 19 | [Phi-3.5-Mini-Instruct](https://huggingface.co/microsoft/Phi-3.5-mini-instruct) | 3.8B | unknown | 32.80% | -18.30% | yes | yes | yes |
| 20 | [CodeGemma-7B-Instruct](https://huggingface.co/google/codegemma-7b-it) | 7B | unknown | 32.30% | -18.80% | yes | yes | yes |
| 21 | [CodeLlama-13B-Base](https://huggingface.co/codellama/CodeLlama-13b-hf) | 13B | unknown | 32.00% | -19.10% | yes | yes | yes |
| 22 | [Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | 8B | 8k | 31.90% | -19.20% | yes | yes | yes |
| 23 | [Phi-3-Small-128K-Instruct](https://huggingface.co/microsoft/Phi-3-small-128k-instruct) | 7B | unknown | 31.10% | -20.00% | yes | yes | yes |
| 24 | [DeepSeek-Coder-V2-Lite-Base](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Base) | 16B / A2.4B | unknown | 30.60% | -20.50% | yes | yes | yes |
| 25 | [Phi-3-Mini-128K-Instruct](https://huggingface.co/microsoft/Phi-3-mini-128k-instruct) | 3.8B | unknown | 29.60% | -21.50% | yes | yes | yes |
| 26 | [Qwen2-7B](https://huggingface.co/Qwen/Qwen2-7B-Instruct) | 7B | unknown | 29.10% | -22.00% | yes | yes | yes |
| 27 | [Llama-3-8B-Base](https://huggingface.co/meta-llama/Meta-Llama-3-8B) | 8B | unknown | 28.80% | -22.30% | yes | yes | yes |
| 28 | [CodeLlama-7B-Base](https://huggingface.co/codellama/CodeLlama-7b-hf) | 7B | unknown | 28.70% | -22.40% | yes | yes | yes |
| 29 | [CodeLlama-13B-Instruct](https://huggingface.co/codellama/CodeLlama-13b-Instruct-hf) | 13B | unknown | 28.50% | -22.60% | yes | yes | yes |
| 30 | [StarCoder2-7B](https://huggingface.co/bigcode/starcoder2-7b) | 7B | unknown | 27.70% | -23.40% | yes | yes | yes |
| 31 | [Qwen2.5-Coder-1.5B](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct) | 1.5B | unknown | 27.00% | -24.10% | yes | yes | yes |
| 32 | [CodeGemma-2B](https://huggingface.co/google/codegemma-2b) | 2B | unknown | 23.90% | -27.20% | yes | yes | yes |
| 33 | [Mistral-7B-v0.3](https://huggingface.co/mistralai/Mistral-7B-v0.3) | 7B | unknown | 23.50% | -27.60% | yes | yes | yes |
| 34 | [Llama-3.2-3B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct) | 3B | unknown | 23.40% | -27.70% | yes | yes | yes |
| 35 | [DeepSeek-Coder-1.3B-Instruct](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-instruct) | 1.3B | unknown | 22.80% | -28.30% | yes | yes | yes |
| 36 | [DeepSeek-Coder-1.3B-Base](https://huggingface.co/deepseek-ai/deepseek-coder-1.3b-base) | 1.3B | unknown | 22.20% | -28.90% | yes | yes | yes |
| 37 | [CodeLlama-7B-Instruct](https://huggingface.co/codellama/CodeLlama-7b-Instruct-hf) | 7B | unknown | 21.90% | -29.20% | yes | yes | yes |
| 38 | [StarCoder2-3B](https://huggingface.co/bigcode/starcoder2-3b) | 3B | unknown | 21.40% | -29.70% | yes | yes | yes |
| 39 | [Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) | 1.5B | unknown | 20.30% | -30.80% | yes | yes | yes |
| 40 | [Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | 7B | unknown | 19.50% | -31.60% | yes | yes | yes |
| 41 | [DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B) | 7B | unknown | 17.50% | -33.60% | yes | yes | yes |
| 42 | [Mistral-Nemo-12B-Instruct](https://huggingface.co/nv-mistralai/Mistral-Nemo-12B-Instruct) | 12B | unknown | 11.50% | -39.60% | yes | yes | yes |
| 43 | [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | 8B | unknown | 10.60% | -40.50% | yes | yes | yes |
| 44 | [Qwen2.5-0.5B](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct) | 0.5B | unknown | 8.80% | -42.30% | yes | yes | yes |
| 45 | [Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct) | 1B | unknown | 8.20% | -42.90% | yes | yes | yes |
| 46 | [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B) | 1.5B | unknown | 7.00% | -44.10% | yes | yes | yes |

## Best Local Fits

- Best open model fitting a single A100 80GB: [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) - 49.70% (109B / A17B, INT4/GGUF estimate)
- Best open model fitting 24GB VRAM: [Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) - 49.00% (32B, INT4/GGUF estimate)

## Notes

Fit estimates use INT4/GGUF weight size with a conservative 15% overhead and do not include full KV-cache growth at long context.
Closed-model gaps are computed as `open score - best closed score` within the same parsed benchmark rows.
