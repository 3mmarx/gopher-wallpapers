#!/usr/bin/env python3
"""Regenerate the wallpaper grid in README.md and the table in PROMPTS.md.

Both files carry HTML comment markers; only the content between them is
rewritten, so hand-written prose above and below survives.

    python3 scripts/update-docs.py [--style pixel-art]
"""
import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
COLUMNS = 3
THUMB_WIDTH = 260


def grid(style: str) -> str:
    src = ROOT / "wallpapers" / style
    names = sorted(p.name for p in src.glob("*.jpg"))
    if not names:
        raise SystemExit(f"no wallpapers found in {src}")

    cells = [
        f'<a href="wallpapers/{style}/{n}">'
        f'<img src="previews/{style}/{n}" width="{THUMB_WIDTH}" alt="{n[:-4]}" loading="lazy">'
        f"</a><br><sub>{n[:-4].replace('-', ' ')}</sub>"
        for n in names
    ]

    rows = []
    header = "| " + " | ".join([" "] * COLUMNS) + " |"
    divider = "|" + "|".join(["---"] * COLUMNS) + "|"
    for i in range(0, len(cells), COLUMNS):
        chunk = cells[i:i + COLUMNS]
        chunk += [""] * (COLUMNS - len(chunk))
        rows.append("| " + " | ".join(chunk) + " |")

    body = "\n".join([header, divider, *rows])
    return f"{body}\n\n<sub>{len(names)} wallpapers · click any thumbnail for the full-resolution image</sub>\n"


def prompts_table(style: str) -> str:
    src = ROOT / "wallpapers" / style
    names = sorted(p.name for p in src.glob("*.jpg"))
    rows = ["| File | Prompt used | Model / settings |", "| --- | --- | --- |"]
    rows += [f"| `{n}` | | |" for n in names]
    return "\n".join(rows) + "\n"


def splice(path: pathlib.Path, begin: str, end: str, content: str) -> bool:
    if not path.exists():
        print(f"  skip {path.name} (missing)")
        return False
    text = path.read_text()
    pattern = re.compile(
        re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(text):
        print(f"  skip {path.name} (markers not found)")
        return False
    path.write_text(pattern.sub(begin + "\n" + content + end, text))
    print(f"  updated {path.name} ({len(content.splitlines())} lines)")
    return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--style", default="pixel-art")
    args = ap.parse_args()

    splice(ROOT / "README.md", "<!-- BEGIN GRID -->", "<!-- END GRID -->", grid(args.style))
    splice(ROOT / "PROMPTS.md", "<!-- BEGIN PROMPTS -->", "<!-- END PROMPTS -->", prompts_table(args.style))
