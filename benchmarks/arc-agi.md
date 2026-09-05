# ARC-AGI

ARC-AGI evaluates adaptation to novel abstract reasoning tasks rather than memorized knowledge.

## What It Measures

Fluid intelligence, abstraction, and adaptation under a task budget.

## Evaluation

Systems solve held-out ARC tasks; the headline score is task success rate.

Official leaderboard or source: [https://arcprize.org/leaderboard](https://arcprize.org/leaderboard)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) | leaderboard | arc_agi_json |
| [ARC Prize leaderboard page](https://arcprize.org/leaderboard) | leaderboard | cache_only |

## Top 10 Overall

| Rank | Model | Open Weight | Params | Score | Source |
| ---- | ----- | ----------- | ------ | ----- | ------ |
| 1 | GPT-6 Astra - Provider Adapter (High) | no | unknown | 99.95% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 2 | GPT-6 Astra - Provider Adapter (Max) | no | unknown | 98.55% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 3 | GPT-6 Astra - Provider Adapter (XHigh) | no | unknown | 98.44% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 4 | GPT-6 Astra - Provider Adapter (Medium) | no | unknown | 98.44% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 5 | GPT-6 Astra - Provider Adapter (Low) | no | unknown | 98.03% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 6 | GPT-6 Astra - Provider Adapter (None) | no | unknown | 96.72% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 7 | GPT-6 Astra (Max) | no | unknown | 62.71% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 8 | GPT-6 Astra (XHigh) | no | unknown | 59.34% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 9 | GPT-6 Astra (High) | no | unknown | 54.82% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 10 | GPT-6 Astra (Medium) | no | unknown | 38.59% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |

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
