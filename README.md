# Local LLM Benchmark Tracker

This repository tracks open-weight LLMs that can realistically be run locally, normalizes model names and parameter counts, and regenerates benchmark Markdown from official sources.

Run the full update with:

```bash
python scripts/update.py
```

Generated tables prioritize official leaderboards and machine-readable assets. Sources that are not yet parseable are still cached and documented on their benchmark page.

## Benchmark Overview

| Benchmark | Task | Best Closed | Best <=20B | Gap | Parsed Rows |
| --------- | ---- | ----------- | ---------- | --- | ----------- |
| [MMLU](benchmarks/mmlu.md) | Academic multitask reasoning and knowledge | n/a | n/a | n/a | 0 |
| [MMLU-Pro](benchmarks/mmlu-pro.md) | Harder academic multiple choice | Gemini 3.1 Pro 91.16% | Qwen3.5-9B 82.50% | -8.66% | 236 |
| [GPQA](benchmarks/gpqa.md) | Graduate-level science QA | n/a | n/a | n/a | 0 |
| [Humanity's Last Exam](benchmarks/hle.md) | Expert-level multimodal reasoning | n/a | n/a | n/a | 0 |
| [ARC-AGI](benchmarks/arc-agi.md) | Abstract reasoning on novel tasks | Claude Opus 4.8 1.52% | n/a | n/a | 7 |
| [SimpleBench](benchmarks/simplebench.md) | Everyday hard reasoning | n/a | n/a | n/a | 0 |
| [HumanEval](benchmarks/humaneval.md) | Python function synthesis | n/a | n/a | n/a | 0 |
| [MBPP](benchmarks/mbpp.md) | Mostly Basic Python Problems | n/a | n/a | n/a | 0 |
| [LiveCodeBench](benchmarks/livecodebench.md) | Contamination-resistant coding | O4-Mini (High) 87.30% | n/a | n/a | 25 |
| [Aider Polyglot](benchmarks/aider-polyglot.md) | Multi-language code editing | GPT-5 88.00% | n/a | n/a | 54 |
| [BigCodeBench](benchmarks/bigcodebench.md) | Practical code generation | [GPT-4o](https://openai.com/index/hello-gpt-4o/) 51.10% | [Qwen2.5-Coder-14B](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) 48.20% | -2.90% | 188 |
| [SWE-bench Verified](benchmarks/swe-bench.md) | Real GitHub issue resolution | claude-4-5-opus 76.80% | n/a | n/a | 34 |
| [SWE-bench Live](benchmarks/swe-bench-live.md) | Continuously updated SWE tasks | n/a | n/a | n/a | 0 |
| [Terminal-Bench](benchmarks/terminal-bench.md) | Terminal task completion | n/a | n/a | n/a | 0 |
| [TAU-Bench](benchmarks/tau-bench.md) | Tool-agent user interaction | n/a | n/a | n/a | 0 |
| [OSWorld](benchmarks/osworld.md) | Computer-use agent tasks | n/a | n/a | n/a | 0 |
| [WebArena](benchmarks/webarena.md) | Web task completion | n/a | n/a | n/a | 0 |
| [WebVoyager](benchmarks/webvoyager.md) | Vision-enabled web navigation | n/a | n/a | n/a | 0 |
| [Berkeley Function Calling Leaderboard](benchmarks/bfcl.md) | Function and tool calling | Gemini 3.1 Pro Preview 83.12% | BitAgent-Bounty-8B 93.12% | +10.00% | 90 |
| [ToolAthlon](benchmarks/toolathlon.md) | Long-horizon tool use | n/a | n/a | n/a | 0 |
| [MCP Atlas](benchmarks/mcp-atlas.md) | MCP server tool-use competency | n/a | n/a | n/a | 0 |
| [LongBench](benchmarks/longbench.md) | Long-context understanding | n/a | n/a | n/a | 0 |
| [RULER](benchmarks/ruler.md) | Synthetic long-context stress tests | n/a | n/a | n/a | 0 |
| [Needle In A Haystack](benchmarks/needle-in-a-haystack.md) | Long-context retrieval | n/a | n/a | n/a | 0 |
| [MMMU](benchmarks/mmmu.md) | Multimodal expert reasoning | n/a | n/a | n/a | 0 |
| [AI2D](benchmarks/ai2d.md) | Diagram question answering | n/a | n/a | n/a | 0 |
| [DocVQA](benchmarks/docvqa.md) | Document visual question answering | n/a | n/a | n/a | 0 |
| [OmniDocBench](benchmarks/omnidocbench.md) | Document parsing and understanding | n/a | n/a | n/a | 0 |

## Coding

### [HumanEval](benchmarks/humaneval.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [MBPP](benchmarks/mbpp.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [LiveCodeBench](benchmarks/livecodebench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [Aider Polyglot](benchmarks/aider-polyglot.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [BigCodeBench](benchmarks/bigcodebench.md)

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


## Software Engineering

### [SWE-bench Verified](benchmarks/swe-bench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [SWE-bench Live](benchmarks/swe-bench-live.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._


## Agent Benchmarks

### [Terminal-Bench](benchmarks/terminal-bench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [TAU-Bench](benchmarks/tau-bench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [OSWorld](benchmarks/osworld.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [WebArena](benchmarks/webarena.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [WebVoyager](benchmarks/webvoyager.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._


## General reasoning

### [MMLU](benchmarks/mmlu.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [MMLU-Pro](benchmarks/mmlu-pro.md)

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

### [GPQA](benchmarks/gpqa.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [Humanity's Last Exam](benchmarks/hle.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [ARC-AGI](benchmarks/arc-agi.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [SimpleBench](benchmarks/simplebench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._


## Tool Use

### [Berkeley Function Calling Leaderboard](benchmarks/bfcl.md)

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

### [ToolAthlon](benchmarks/toolathlon.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [MCP Atlas](benchmarks/mcp-atlas.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._


## Long Context

### [LongBench](benchmarks/longbench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [RULER](benchmarks/ruler.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [Needle In A Haystack](benchmarks/needle-in-a-haystack.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._


## Vision

### [MMMU](benchmarks/mmmu.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [AI2D](benchmarks/ai2d.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [DocVQA](benchmarks/docvqa.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

### [OmniDocBench](benchmarks/omnidocbench.md)

_No source-attributed open-weight <=20B rows are available from parseable sources yet._

## Repository Layout

- `data/benchmarks.json` documents benchmarks and official sources.
- `data/models.json` stores model metadata used for local-fit estimates.
- `data/aliases.json` stores explicit alias merges.
- `data/generated/records.json` stores normalized generated rows.
- `benchmarks/*.md` and this README are generated by `python scripts/update.py`.

## Automation

The GitHub Actions workflow in `.github/workflows/update.yml` can run the updater on a schedule and open a pull request when generated tables change.
