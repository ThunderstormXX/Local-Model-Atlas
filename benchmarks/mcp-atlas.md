# MCP Atlas

MCP Atlas evaluates tool-use competency across real Model Context Protocol servers and tools.

## What It Measures

Multi-server tool coordination, tool selection, and agent workflow completion.

## Evaluation

Agents complete MCP-backed tasks; public leaderboards report pass rate.

Official leaderboard or source: [https://labs.scale.com/leaderboard/mcp_atlas](https://labs.scale.com/leaderboard/mcp_atlas)

## Source Coverage

| Source | Type | Parser |
| ------ | ---- | ------ |
| [Scale Labs MCP Atlas leaderboard](https://labs.scale.com/leaderboard/mcp_atlas) | leaderboard | cache_only |
| [MCP Atlas repository](https://github.com/scaleapi/mcp-atlas) | repository | cache_only |

## Top 10 Overall

_No rows parsed yet._

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
