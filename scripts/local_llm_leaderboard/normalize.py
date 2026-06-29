from __future__ import annotations

import html
import re
from typing import Any, Iterable


QUALIFIER_RE = re.compile(
    r"\b(fc|prompt|thinking|max|high|low|medium|reasoning|instruct|chat)\b",
    re.IGNORECASE,
)


def clean_model_name(raw: str) -> str:
    value = html.unescape(str(raw or "")).strip()
    value = re.sub(r"<[^>]+>", "", value)
    value = value.replace("_", "-")
    value = value.replace("–", "-").replace("—", "-")
    value = re.sub(r"\s+", " ", value)
    value = value.strip(" -")

    if value.startswith("https://huggingface.co/"):
        value = value.removeprefix("https://huggingface.co/").strip("/")
        parts = value.split("/")
        if len(parts) >= 2:
            value = parts[-1]

    return value


def fingerprint(raw: str) -> str:
    value = clean_model_name(raw).lower()
    value = re.sub(r"https?://huggingface\.co/", "", value)
    value = re.sub(r"^[a-z0-9_.-]+/", "", value)
    value = re.sub(r"\([^)]*\)", " ", value)
    value = QUALIFIER_RE.sub(" ", value)
    value = re.sub(r"[^a-z0-9]+", "", value)
    return value


def build_alias_map(alias_rows: Iterable[dict[str, Any]]) -> dict[str, str]:
    alias_map: dict[str, str] = {}
    for row in alias_rows:
        canonical = clean_model_name(row["canonical"])
        alias_map[fingerprint(canonical)] = canonical
        for alias in row.get("aliases", []):
            alias_map[fingerprint(alias)] = canonical
    return alias_map


def normalize_model_name(raw: str, alias_map: dict[str, str] | None = None) -> str:
    cleaned = clean_model_name(raw)
    fp = fingerprint(cleaned)
    if alias_map and fp in alias_map:
        return alias_map[fp]

    lower = cleaned.lower()
    compact = fp

    if re.search(r"\bgpt[- ]?5[.-]?5\b", lower) or "gpt552026" in compact:
        return "GPT-5.5"
    if re.search(r"\bgpt[- ]?5\b", lower):
        return "GPT-5"
    if "gpt4o" in compact:
        return "GPT-4o"
    if re.fullmatch(r"o[134](mini)?", compact) or compact.startswith(("o1", "o3", "o4")):
        return cleaned

    if "claudeopus48" in compact:
        return "Claude Opus 4.8"
    if "claudeopus46" in compact or "anthropicopus46" in compact:
        return "Claude Opus 4.6"
    if "claudesonnet45" in compact or "claudesonnet4520250929" in compact:
        return "Claude Sonnet 4.5"

    gemini_match = re.search(r"gemini[- ]?(\d)(?:[.-](\d))?[- ]?(pro|flash)?", lower)
    if gemini_match and not lower.startswith("gemma"):
        major, minor, tier = gemini_match.groups()
        suffix = f" {tier.title()}" if tier else ""
        version = f"{major}.{minor}" if minor else major
        if "preview" in lower:
            suffix += " Preview"
        return f"Gemini {version}{suffix}".strip()

    qwen_match = re.search(r"qwen/?(qwen)?(?P<version>\d(?:\.\d)?)(?:[- ]?coder)?[- ]?(?P<size>\d+(?:\.\d+)?)b", lower)
    if qwen_match:
        version = qwen_match.group("version")
        size = qwen_match.group("size")
        coder = "Coder-" if "coder" in lower else ""
        return f"Qwen{version}-{coder}{size}B"

    if "deepseekv3" in compact:
        if "0324" in compact:
            return "DeepSeek-V3-0324"
        return "DeepSeek-V3"
    if "deepseekr1distillqwen14b" in compact:
        return "DeepSeek-R1-Distill-Qwen-14B"

    glm_match = re.search(r"glm[- ]?(\d(?:\.\d)?)", lower)
    if glm_match:
        return f"GLM-{glm_match.group(1)}"

    if "kimi" in lower and "k2" in lower:
        if "2.5" in lower or "25" in compact:
            return "Kimi-K2.5"
        return "Kimi-K2-Instruct"

    if lower.startswith("meta-llama/"):
        return cleaned.split("/", 1)[1]
    if lower.startswith(("qwen/", "google/", "mistralai/", "deepseek-ai/", "zai-org/", "moonshot/")):
        return cleaned.split("/", 1)[1]

    return cleaned


def parse_param_counts(raw: str) -> tuple[float | None, float | None]:
    value = clean_model_name(raw)

    moe = re.search(r"(?P<total>\d+(?:\.\d+)?)\s*[bB]\s*[-_ ]?[aA](?P<active>\d+(?:\.\d+)?)\s*[bB]", value)
    if moe:
        return float(moe.group("total")), float(moe.group("active"))

    times = re.search(r"(?P<count>\d+)\s*x\s*(?P<size>\d+(?:\.\d+)?)\s*[bB]", value, re.IGNORECASE)
    if times:
        count = float(times.group("count"))
        size = float(times.group("size"))
        return count * size, None

    all_sizes = re.findall(r"(?<![a-zA-Z])(\d+(?:\.\d+)?)\s*[bB]\b", value)
    if all_sizes:
        return float(all_sizes[-1]), float(all_sizes[-1])

    return None, None


def param_bucket(total_params_b: float | None) -> str:
    if total_params_b is None:
        return "unknown"
    if total_params_b <= 7:
        return "<=7B"
    if total_params_b <= 14:
        return "<=14B"
    if total_params_b <= 20:
        return "<=20B"
    if total_params_b <= 32:
        return "<=32B"
    if total_params_b <= 40:
        return "<=40B"
    if total_params_b <= 70:
        return "<=70B"
    return ">70B"


def infer_organization(name: str) -> str | None:
    lower = name.lower()
    if lower.startswith(("gpt", "o1", "o3", "o4", "openai/")):
        return "OpenAI"
    if "claude" in lower or lower.startswith("anthropic"):
        return "Anthropic"
    if lower.startswith("gemini"):
        return "Google"
    if lower.startswith("gemma") or "google/gemma" in lower:
        return "Google"
    if lower.startswith(("qwen", "qwq")) or "qwen/" in lower:
        return "Qwen"
    if lower.startswith("llama") or "meta-llama" in lower:
        return "Meta"
    if lower.startswith("deepseek"):
        return "DeepSeek"
    if lower.startswith(("mistral", "mixtral", "devstral")):
        return "Mistral AI"
    if lower.startswith("glm") or lower.startswith("zai") or "z.ai" in lower:
        return "Z.ai"
    if lower.startswith("kimi"):
        return "Moonshot AI"
    if lower.startswith("grok") or "xai" in lower:
        return "xAI"
    if lower.startswith("amazon") or "nova" in lower:
        return "Amazon"
    if lower.startswith("bitagent"):
        return "BitAgent"
    if lower.startswith("arch-agent"):
        return "Katanemo"
    return None


def infer_open_weight(name: str, organization: str | None = None) -> bool | None:
    lower = name.lower()
    org = (organization or "").lower()
    closed_markers = (
        "gpt",
        "claude",
        "gemini",
        "grok",
        "o1",
        "o3",
        "o4",
        "amazon-nova",
        "mistral-large",
        "mistral-medium",
    )
    open_markers = (
        "qwen",
        "llama",
        "gemma",
        "mistral",
        "mixtral",
        "devstral",
        "deepseek",
        "glm",
        "kimi-k2",
        "phi",
        "starcoder",
        "codegemma",
        "codeqwen",
        "magicoder",
        "bitagent",
        "arch-agent",
        "gpt-oss",
        "swe-llama",
    )
    if lower.startswith("gpt-oss") or "gpt-oss" in lower:
        return True
    if any(lower.startswith(marker) or marker in lower for marker in closed_markers):
        return False
    if any(lower.startswith(marker) or marker in lower for marker in open_markers):
        return True
    if org in {"openai", "anthropic", "xai", "amazon"}:
        return False
    if org in {"qwen", "meta", "deepseek", "mistral ai", "z.ai", "moonshot ai"}:
        return True
    return None


def estimate_vram_gb(total_params_b: float | None) -> dict[str, float | None]:
    if total_params_b is None:
        return {"fp16_bf16": None, "int8": None, "int4_gguf": None}
    overhead = 1.15
    return {
        "fp16_bf16": round(total_params_b * 2.0 * overhead, 1),
        "int8": round(total_params_b * 1.0 * overhead, 1),
        "int4_gguf": round(total_params_b * 0.5 * overhead, 1),
    }


def fits_vram(total_params_b: float | None, capacity_gb: int) -> bool | None:
    estimate = estimate_vram_gb(total_params_b)["int4_gguf"]
    if estimate is None:
        return None
    return estimate <= capacity_gb * 0.85
