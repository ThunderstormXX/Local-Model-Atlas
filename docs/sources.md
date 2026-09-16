# Data Sources

Every benchmark source registered for the updater is listed below. `Records` is the number of score rows parsed from that source during the latest run.

| Benchmark | Source | Parser | Records | Cache |
| --------- | ------ | ------ | ------- | ----- |
| MMLU | [MMLU paper](https://arxiv.org/abs/2009.03300) | cache_only | 0 | data/cache/0635974beafcf9c5.html |
| MMLU | [OpenCompass LLM leaderboard](https://opencompass.org.cn/leaderboard-llm) | cache_only | 0 | data/cache/156b0de82b276a43.html |
| MMLU-Pro | [TIGER-Lab MMLU-Pro leaderboard CSV](https://huggingface.co/datasets/TIGER-Lab/mmlu_pro_leaderboard_submission/raw/main/results.csv) | mmlu_pro_csv | 262 | data/cache/83b5ebb1f74f9fde.csv |
| MMLU-Pro | [TIGER-Lab MMLU-Pro Hugging Face Space](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro) | cache_only | 0 | data/cache/17491a9ebd86f60d.html |
| GPQA | [GPQA benchmark repository](https://github.com/idavidrein/gpqa) | cache_only | 0 | data/cache/e2bd9cf805378855.html |
| GPQA | [Artificial Analysis intelligence leaderboard](https://artificialanalysis.ai/leaderboards/models) | cache_only | 0 | data/cache/223f4e31d7862bfc.html |
| Humanity's Last Exam | [Humanity's Last Exam official site](https://lastexam.ai/) | cache_only | 0 | data/cache/05665ed86ec75ee7.html |
| ARC-AGI | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) | arc_agi_json | 39 | data/cache/c17ff3effa79c1ab.json |
| ARC-AGI | [ARC Prize leaderboard page](https://arcprize.org/leaderboard) | cache_only | 0 | data/cache/a27f2ad202a2b5a7.html |
| SimpleBench | [SimpleBench official site](https://simple-bench.com/) | cache_only | 0 | data/cache/74442715952b612f.html |
| HumanEval | [OpenAI HumanEval repository](https://github.com/openai/human-eval) | cache_only | 0 | data/cache/9edbbd4ae30cd1f8.html |
| HumanEval | [EvalPlus leaderboard](https://evalplus.github.io/leaderboard.html) | cache_only | 0 | data/cache/4db0fce60f99336f.html |
| MBPP | [Google Research MBPP repository](https://github.com/google-research/google-research/tree/master/mbpp) | cache_only | 0 | data/cache/cf014c7338fe7162.html |
| MBPP | [EvalPlus leaderboard](https://evalplus.github.io/leaderboard.html) | cache_only | 0 | data/cache/4db0fce60f99336f.html |
| LiveCodeBench | [LiveCodeBench performance JSON](https://livecodebench.github.io/performances_generation.json) | livecodebench_generation_json | 28 | data/cache/d1ff617616401c53.json |
| LiveCodeBench | [LiveCodeBench leaderboard page](https://livecodebench.github.io/leaderboard.html) | cache_only | 0 | data/cache/c907c4f9f74df324.html |
| Aider Polyglot | [Aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) | aider_polyglot_html | 69 | data/cache/5b92e98d55fe64ec.html |
| BigCodeBench | [BigCodeBench complete/instruct JSON](https://bigcode-bench.github.io/results.json) | bigcodebench_json | 156 | data/cache/ee63a6d1e7e072ff.json |
| BigCodeBench | [BigCodeBench hard JSON](https://bigcode-bench.github.io/results-hard.json) | bigcodebench_json | 202 | data/cache/ff944c0d8157101d.json |
| SWE-bench Verified | [SWE-bench embedded official leaderboard data](https://www.swebench.com/index.html) | swebench_embedded_json | 0 | data/cache/af84bec01ced42d4.html |
| SWE-bench Verified | [SWE-bench Verified description](https://www.swebench.com/verified.html) | cache_only | 0 | data/cache/af47372f0f81cf3e.html |
| SWE-bench Live | [Microsoft SWE-bench-Live repository](https://github.com/microsoft/SWE-bench-Live) | cache_only | 0 | data/cache/aca51d6c991912b5.html |
| SWE-bench Live | [Live-SWE-agent leaderboard](https://live-swe-agent.github.io/) | cache_only | 0 | data/cache/f5d167c2f8e10958.html |
| Terminal-Bench | [Terminal-Bench official leaderboard](https://www.tbench.ai/leaderboard/terminal-bench/2.0) | cache_only | 0 | data/cache/f49724e280dad652.html |
| TAU-Bench | [TAU-Bench repository](https://github.com/sierra-research/tau-bench) | cache_only | 0 | data/cache/0336f717029b0831.html |
| OSWorld | [OSWorld official leaderboard](https://os-world.github.io/) | cache_only | 0 | data/cache/c819ef71cbf34802.html |
| WebArena | [WebArena official site](https://webarena.dev/) | cache_only | 0 | data/cache/c2614357fa198ba4.html |
| WebVoyager | [WebVoyager repository](https://github.com/MinorJerry/WebVoyager) | cache_only | 0 | data/cache/4f873365eac72f15.html |
| Berkeley Function Calling Leaderboard | [BFCL live leaderboard CSV](https://gorilla.cs.berkeley.edu/data_live.csv) | bfcl_csv | 109 | data/cache/90ef69f7920d307b.csv |
| Berkeley Function Calling Leaderboard | [BFCL official leaderboard page](https://gorilla.cs.berkeley.edu/leaderboard.html) | cache_only | 0 | data/cache/c62226dacccbe98a.html |
| ToolAthlon | [ToolAthlon repository](https://github.com/hkust-nlp/Toolathlon) | cache_only | 0 | data/cache/6502e4e2cd84136a.html |
| MCP Atlas | [Scale Labs MCP Atlas leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) | cache_only | 0 | data/cache/19f038745d5382db.html |
| MCP Atlas | [MCP Atlas repository](https://github.com/scaleapi/mcp-atlas) | cache_only | 0 | data/cache/0fede154f4259f72.html |
| LongBench | [LongBench repository](https://github.com/THUDM/LongBench) | cache_only | 0 | data/cache/0e05f5f9fb86ec43.html |
| RULER | [NVIDIA RULER repository](https://github.com/NVIDIA/RULER) | cache_only | 0 | data/cache/84836b317e20b3b8.html |
| Needle In A Haystack | [Needle In A Haystack repository](https://github.com/gkamradt/LLMTest_NeedleInAHaystack) | cache_only | 0 | data/cache/17f8e83fab7b0fa7.html |
| MMMU | [MMMU official leaderboard](https://mmmu-benchmark.github.io/) | cache_only | 0 | data/cache/289800e50579f28e.html |
| AI2D | [AI2D dataset page](https://allenai.org/data/diagrams) | cache_only | 0 | data/cache/2be2ceed58521a2f.html |
| AI2D | [OpenCompass VLM leaderboard](https://opencompass.org.cn/leaderboard-multimodal) | cache_only | 0 | data/cache/f64c9cc923072459.html |
| DocVQA | [DocVQA official challenge](https://rrc.cvc.uab.es/?ch=17) | cache_only | 0 | data/cache/19f3805a01f36d22.html |
| OmniDocBench | [OmniDocBench repository](https://github.com/opendatalab/OmniDocBench) | cache_only | 0 | data/cache/c099fb6149f5b631.html |
