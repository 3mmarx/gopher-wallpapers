# Contributing

Wallpapers are welcome. This file is the whole rulebook.

## Adding a wallpaper

1. Drop the full-resolution image into `wallpapers/<style>/`.
2. Generate the preview and refresh the gallery:

   ```sh
   ./scripts/make-previews.sh
   python3 scripts/update-docs.py
   ```

3. Add the prompt you used to `PROMPTS.md`.
4. Commit both the wallpaper and its preview — a wallpaper without a preview
   won't show up in the gallery.

## Naming

- **kebab-case**, lowercase, `.jpg`. No spaces, no capitals, no dates.
- **No `gopher-` / `gophers-` prefix.** The repo name carries that context.
  The filename should describe the scene, not the cast.
- **Describe what's happening, then where.** `roasting-chestnuts-in-the-rain`,
  not `chestnuts`.
- **Don't start a filename with a preposition.** `library-at-night`, not
  `in-the-library`. Prepositions belong at the end or get folded into a noun.
- **Time of day only when it defines the image.** Most of this collection is
  set at night, so `-at-night` earns its place only when a daytime twin exists.
- One image, one filename. Don't add `-2`, `-3` or `-v2`; if two images are
  genuinely different scenes, name the difference.

Existing examples, in order of how much they tell you:

```
zen-garden.jpg
train-at-night.jpg            (willow + snow outside)
camping-on-the-cliffs.jpg     (tents on a ledge, mountains behind)
coding-at-the-beach-campfire.jpg
```

## Image specs

| | |
| --- | --- |
| Format | JPEG |
| Resolution | 2752 × 1536 (16:9) |
| Quality | q82 via `scripts/reencode.sh` |
| Previews | 960 px wide, q70, in `previews/<style>/` |

Don't commit re-encoded or resized copies of an already-published wallpaper.
`reencode.sh` reads from `_backup/originals/` so quality never degrades
across runs — but that folder is local-only and isn't part of the repo.

## Adding a new style

A style is just a folder pair. No code changes, no config:

```
wallpapers/<new-style>/
previews/<new-style>/
```

Then run `./scripts/reencode.sh` and `./scripts/make-previews.sh` (adjust the
paths inside for the new style), add a row to the styles table in `README.md`,
and re-run `python3 scripts/update-docs.py --style <new-style>`.

## A note on the gopher

The Go gopher is a trademark of Google LLC. Don't submit the official mascot
artwork or anything derived from it. Original pixel-art gophers are fine.

## Licensing

Contributions are accepted under [CC0 1.0](LICENSE), matching the rest of the
repo. By opening a pull request you agree your image is dedicated to the
public domain.
