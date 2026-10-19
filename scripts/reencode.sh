#!/usr/bin/env bash
# Re-encode every wallpaper at a fixed quality, reading from the originals
# snapshot and writing into wallpapers/<style>/. Idempotent: it always starts
# from _backup/originals/ so repeated runs never compound JPEG generation loss.
set -euo pipefail

QUALITY="${QUALITY:-82}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/_backup/originals"
DST="$ROOT/wallpapers/pixel-art"

[ -d "$SRC" ] || { echo "missing $SRC — nothing to encode" >&2; exit 1; }
mkdir -p "$DST"

for f in "$SRC"/*.jpg; do
  name="$(basename "$f")"
  sips -s format jpeg -s formatOptions "$QUALITY" "$f" --out "$DST/$name" >/dev/null
  printf '  %s\n' "$name"
done

echo "done -> $DST ($(du -sh "$DST" | cut -f1))"
