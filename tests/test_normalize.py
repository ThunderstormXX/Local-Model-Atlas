import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from local_llm_leaderboard.normalize import (
    build_alias_map,
    estimate_vram_gb,
    fits_vram,
    infer_open_weight,
    normalize_model_name,
    param_bucket,
    parse_param_counts,
)


ALIASES = build_alias_map(
    [
        {
            "canonical": "Qwen3-Coder-30B-A3B-Instruct",
            "aliases": [
                "Qwen3 Coder 30B",
                "Qwen3-30B-A3B",
                "https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct",
            ],
        }
    ]
)


class NormalizeTests(unittest.TestCase):
    def test_qwen_coder_aliases_collapse(self):
        names = [
            "Qwen3-Coder-30B-A3B-Instruct",
            "Qwen3 Coder 30B",
            "Qwen3-30B-A3B",
            "https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct",
        ]
        self.assertEqual(
            {normalize_model_name(name, ALIASES) for name in names},
            {"Qwen3-Coder-30B-A3B-Instruct"},
        )

    def test_frontier_name_families_normalize(self):
        self.assertEqual(normalize_model_name("gpt-5-5-2026-04-23-thinking", ALIASES), "GPT-5.5")
        self.assertEqual(normalize_model_name("Claude-Sonnet-4-5-20250929 (FC)", ALIASES), "Claude Sonnet 4.5")
        self.assertEqual(normalize_model_name("gemini-3-1-pro-preview", ALIASES), "Gemini 3.1 Pro Preview")

    def test_param_count_parsing(self):
        self.assertEqual(parse_param_counts("Qwen3-Coder-30B-A3B-Instruct"), (30.0, 3.0))
        self.assertEqual(parse_param_counts("Mixtral-8x7B-Instruct-v0.1"), (56.0, None))
        self.assertEqual(parse_param_counts("Llama-3.1-8B-Instruct"), (8.0, 8.0))

    def test_vram_and_buckets(self):
        self.assertEqual(param_bucket(6.7), "<=7B")
        self.assertEqual(param_bucket(14), "<=14B")
        self.assertEqual(param_bucket(20), "<=20B")
        self.assertEqual(param_bucket(70), "<=70B")
        self.assertEqual(param_bucket(120), ">70B")
        self.assertEqual(estimate_vram_gb(14)["int4_gguf"], 8.0)
        self.assertTrue(fits_vram(14, 24))
        self.assertFalse(fits_vram(70, 24))

    def test_mistral_large_is_not_open_by_family_name(self):
        self.assertFalse(infer_open_weight("mistral-large-2411 (FC)", "Mistral AI"))
        self.assertTrue(infer_open_weight("Mistral-7B-Instruct-v0.2", "Mistral AI"))
        self.assertTrue(infer_open_weight("GPT-oss-20B(high)", "OpenAI"))


if __name__ == "__main__":
    unittest.main()
