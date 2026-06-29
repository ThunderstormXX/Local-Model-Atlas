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
| 1 | Claude Opus 4.8 | no | unknown | 1.52% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 2 | Claude Opus 4.6 | no | unknown | 0.51% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 3 | GPT-5.5 | no | unknown | 0.43% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 4 | Gemini 3.1 Pro Preview | no | unknown | 0.42% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 5 | GPT-5 | no | unknown | 0.21% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 6 | Opus 4.7 (High) | no | unknown | 0.18% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |
| 7 | Grok 4.20 (Beta Reasoning) | no | unknown | 0.09% | [ARC Prize v3 leaderboard JSON](https://arcprize.org/media/data/leaderboard/v3.json) |

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
