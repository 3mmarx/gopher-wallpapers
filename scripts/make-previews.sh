#!/usr/bin/env bash
# Generate the lightweight thumbnails the README grid links to.
# One preview per wallpaper, same basename, same relative layout.
set -euo pipefail

SIZE="${SIZE:-960}"
QUALITY="${QUALITY:-70}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/wallpapers/pixel-art"
DST="$ROOT/previews/pixel-art"

mkdir -p "$DST"

for f in "$SRC"/*.jpg; do
  name="$(basename "$f")"
  # downscale first, then re-encode: avoids running JPEG compression on a
  # full-resolution image just to throw 90% of the data away.
  sips -Z "$SIZE" "$f" --out "$DST/$name" >/dev/null
  sips -s format jpeg -s formatOptions "$QUALITY" "$DST/$name" >/dev/null
  printf '  %s\n' "$name"
done

echo "done -> $DST ($(du -sh "$DST" | cut -f1))"
