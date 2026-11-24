import base64
import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import refresh_numbers as rn  # noqa: E402

STATS = rn.Stats(contributions=1243, commits=567, pull_requests=143)
DAY = datetime.date(2026, 11, 24)
BLOCK = "a\n<!-- numbers:start -->\n{}\n<!-- numbers:end -->\nb\n"


class RenderLine(unittest.TestCase):
    def test_render_english(self):
        self.assertEqual(
            rn.render_line(STATS, "en", DAY),
            "**1,243** contributions in the last 12 months · **567** commits"
            " · **143** pull requests · updated 2026-11-24",
        )

    def test_render_chinese(self):
        self.assertEqual(
            rn.render_line(STATS, "zh", DAY),
            "过去 12 个月：**1,243** 次贡献 · **567** 次提交 · **143** 个 PR · 更新于 2026-11-24",
        )


class SwapBlock(unittest.TestCase):
    def test_swap_replaces_only_the_block(self):
        self.assertEqual(rn.swap_block(BLOCK.format("old"), "new"), BLOCK.format("new"))

    def test_swap_missing_marker_raises(self):
        with self.assertRaises(ValueError):
            rn.swap_block("no markers here\n", "new")

    def test_swap_duplicate_marker_raises(self):
        with self.assertRaises(ValueError):
            rn.swap_block(BLOCK.format("old") + BLOCK.format("old"), "new")

    def test_swap_keeps_crlf(self):
        crlf = BLOCK.format("old").replace("\n", "\r\n")
        self.assertEqual(rn.swap_block(crlf, "new"), BLOCK.format("new").replace("\n", "\r\n"))


class SameNumbers(unittest.TestCase):
    def test_same_numbers_ignores_date(self):
        old = BLOCK.format(rn.render_line(STATS, "en", datetime.date(2026, 11, 17)))
        new = BLOCK.format(rn.render_line(STATS, "en", DAY))
        self.assertTrue(rn.same_numbers(old, new))

    def test_same_numbers_detects_change(self):
        old = BLOCK.format(rn.render_line(STATS, "en", DAY))
        new = BLOCK.format(rn.render_line(STATS._replace(commits=570), "en", DAY))
        self.assertFalse(rn.same_numbers(old, new))


class EncodeAddition(unittest.TestCase):
    def test_encode_addition_round_trips_chinese(self):
        add = rn.encode_addition("README.zh-CN.md", "过去 12 个月")
        self.assertEqual(base64.b64decode(add["contents"]).decode("utf-8"), "过去 12 个月")
        self.assertEqual(add["path"], "README.zh-CN.md")


if __name__ == "__main__":
    unittest.main()
