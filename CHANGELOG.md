# Changelog

## 0.1.1 — 2026-11-16

- Fixed: `mens-color-analysis` and `mens-style-advisor` descriptions are now quoted, so strict YAML loaders (e.g. Perplexity) accept the frontmatter

## 0.1.0 — 2026-11-16

Initial version.

- `mens-style-profile`: one short profile (body, taste, photo check, color, grooming, wardrobe) that all other skills read; beginner-friendly setup in small steps
- `mens-color-analysis`: season, palettes with hex codes and colors to avoid near the face; drape images of colors and metals on his own photo (`scripts/make_drapes.py`); earlier results compared, not silently replaced; owned colors sorted into near face / lower body / with buffer
- `mens-grooming`: beard options rated with mm and a length scale, lines and color; shaved-head or haircut care; care zones and a numbered routine; best glasses frame, even without glasses
- `mens-style-advisor`: outfits from his own clothes, occasion outfits, weekly rotation, outfit check, signature look; opinionated `style-principles.md`; no shopping unless asked
- `mens-travel-packing`: packing list from his own wardrobe for the destination's weather, dress code, trip length, laundry and luggage, with outfits and an entry-rule heads-up
- `mens-style-book`: illustrated personal style guide (rule → why → picture → ✓/✗) in nine pages, with drapes, zone map, beard options, glasses and a best-look summary; `scripts/prepare_images.py` for converting and face-aware cropping, `assets/schematics.md` for beard and frame drawings
- Photo check before every analysis; photos never stored; evals for every skill; Claude Code plugin and marketplace files
