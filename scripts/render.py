#!/usr/bin/env python3
"""Render the news-summary image for the make.fun bounty
"Sum up 19 November's world news in one image" (news-image-20261119).

Output: assets/entry.png — 1024x1024 PNG, code-rendered with PIL only
(no AI image generation, no network, no external assets).
"""
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = Path(__file__).resolve().parent.parent / "assets" / "entry.png"

PAPER = (250, 247, 240)      # warm off-white
NAVY = (16, 38, 59)          # header band
INK = (20, 32, 46)           # headline ink
BODY = (61, 74, 87)          # summary ink
MUTED = (120, 128, 138)      # footer / rules
GOLD = (232, 179, 75)        # date line
RULE = (214, 208, 196)       # divider lines

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
SERIF_B = ImageFont.truetype(str(FONT_DIR / "DejaVuSerif-Bold.ttf"), 66)
SERIF_I = ImageFont.truetype(str(FONT_DIR / "DejaVuSerif.ttf"), 24)
SANS_B = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), 31)
SANS = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 23)
SANS_SM = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 20)
TAG = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), 21)
NUM = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), 26)

STORIES = [
    {
        "tag": "SUMMIT",
        "color": (29, 78, 137),
        "headline": "Trump, Xi & Putin meet in Shenzhen",
        "summary": "The three leaders hold their first trilateral summit, with nuclear arms, Ukraine and the Iran war on the agenda.",
    },
    {
        "tag": "GULF STRIKES",
        "color": (180, 35, 24),
        "headline": "US and Iran trade strikes across the Gulf",
        "summary": "Iran fires on US bases in Kuwait and Bahrain; the US hits a missile site on Qeshm Island, and a tanker is struck in Hormuz.",
    },
    {
        "tag": "GTA 6",
        "color": (109, 40, 217),
        "headline": "GTA 6 launches worldwide today",
        "summary": "Rockstar's most anticipated game arrives today — 1,600 developers in Bengaluru helped build it.",
    },
    {
        "tag": "CRIMEA",
        "color": (194, 65, 12),
        "headline": "Ukraine hits Crimean Bridge again",
        "summary": "Kyiv strikes the bridge for the third time this week as the war grinds on.",
    },
    {
        "tag": "JUSTICE",
        "color": (15, 118, 110),
        "headline": "UN court to rule on Myanmar genocide case",
        "summary": "The world's top court prepares its verdict on the Rohingya genocide claims against Myanmar.",
    },
]


def wrap(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    """Greedy word wrap; returns at most 2 lines (raises if it needs more)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if len(lines) > 2:
        raise ValueError(f"summary needs {len(lines)} lines (>2): {text!r}")
    return lines


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- Header band ---
    d.rectangle([0, 0, W, 148], fill=NAVY)
    title = "THE WORLD TODAY"
    tw = d.textlength(title, font=SERIF_B)
    d.text(((W - tw) / 2, 26), title, font=SERIF_B, fill=(255, 255, 255))
    date = "T H U R S D A Y  ·  1 9  N O V E M B E R  2 0 2 6"
    dw = d.textlength(date, font=SANS_SM)
    d.text(((W - dw) / 2, 106), date, font=SANS_SM, fill=GOLD)

    # --- Kicker ---
    kick = "Five stories that defined the day"
    kw = d.textlength(kick, font=SERIF_I)
    d.text(((W - kw) / 2, 160), kick, font=SERIF_I, fill=BODY)
    d.line([48, 196, W - 48, 196], fill=RULE, width=2)

    # --- Story rows ---
    text_x = 132
    text_w = W - 48 - text_x  # 844
    row_top = 210
    row_h = 146
    gap = 10
    for i, s in enumerate(STORIES):
        y = row_top + i * (row_h + gap)
        # number circle
        d.ellipse([48, y + 8, 104, y + 64], fill=s["color"])
        num = f"{i + 1}"
        nw = d.textlength(num, font=NUM)
        d.text((48 + (56 - nw) / 2, y + 18), num, font=NUM, fill=(255, 255, 255))
        # tag line
        d.text((text_x, y + 2), s["tag"], font=TAG, fill=s["color"])
        # headline
        d.text((text_x, y + 30), s["headline"], font=SANS_B, fill=INK)
        # summary (max 2 lines)
        lines = wrap(d, s["summary"], SANS, text_w)
        for j, line in enumerate(lines):
            d.text((text_x, y + 74 + j * 30), line, font=SANS, fill=BODY)
        # divider (not after the last row)
        if i < len(STORIES) - 1:
            d.line([48, y + row_h - 4, W - 48, y + row_h - 4], fill=RULE, width=2)

    # --- Footer ---
    foot = "Summarised from major news outlets  ·  19 November 2026"
    fw = d.textlength(foot, font=SANS_SM)
    d.text(((W - fw) / 2, 966), foot, font=SANS_SM, fill=MUTED)
    note = "Code-rendered summary image"
    nw = d.textlength(note, font=SANS_SM)
    d.text(((W - nw) / 2, 992), note, font=SANS_SM, fill=MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print(f"wrote {OUT}  {OUT.stat().st_size} bytes  {img.size}")


if __name__ == "__main__":
    main()
