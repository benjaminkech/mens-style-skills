---
name: mens-color-analysis
description: Use when a man wants a personal color analysis from a face photo: undertone, contrast, season, best and worst colors, metals, drape images that show colors on his own face, and how to use colors he already owns. Also use when he asks which colors suit him, how a color looks on him, or why an earlier color result differs.
---

# Men's Color Analysis

From **one or two face photos**, determine his coloring and give a palette he can apply to clothes he already owns. Shopping is not the goal. Answer in the user's language. The user may be advising someone else — address that person, and only analyze photos of someone who agreed to it.

If `STYLE-PROFILE.md` exists, read it first. The palette decides **which colors suit him near the face**; how colors combine in an outfit is covered by `mens-style-advisor`.

**Caveat to state once:** seasonal color analysis is a practical tool, not a science. A phone photo gives an estimate; treat the result as a starting point and trust what he sees in the mirror.

## Photo

One good photo is enough. **Check it first** with `mens-style-profile/references/photo-check.md` (skip if the profile already records a verdict for this photo). Good → analyze. Usable with limits → analyze and cap the affected findings' confidence. Not usable → say why in one sentence and ask for one better photo with the checklist's tips; if the second is still not usable, give estimates only. Optional for higher confidence: one selfie in a plain white top and one in black. Never ask for more.

State confidence for each finding (high / medium / estimate) and what would improve it. Never invent features that aren't visible. Describe skin only in color terms (tone, undertone, depth); never label ethnicity.

## Earlier results

Look for an earlier color analysis first: in the profile, the project, or the conversation. Seasons read from phone photos drift with the light, so a new label that contradicts the old one confuses more than it helps.
- **Same result:** say so and raise confidence.
- **Different result:** don't silently replace it. Name both, say what likely explains the gap (light, white balance, a greyer beard, a shaved head), and settle it with the drape test below, using the deciding colors of both seasons. Record the outcome so the next run starts from it.

## Analysis

Undertone, depth, contrast (note when a shaved head or grey hair changes it), chroma, brightness, and a 12-season label with runner-up. Rate contrast, depth and brightness on a simple low–medium–high scale too, so they can be shown as meters. Note visible features that change color choices (e.g. natural redness, no hair framing the face, glasses frame color).

## Deliver

All palettes with names and hex codes:
- Best neutrals, best base colors, 1–3 accents
- Which white (optic, soft white, ecru) and which metals
- Colors to avoid **near the face**, each with the reason
- How best vs. avoid colors change his skin, eyes, contours and overall presence
- A few business and casual combinations in his palette

## Colors on you (drape test)

Telling him "navy suits you" is weaker than showing it. If there is a usable photo, make drape images: the same photo with a flat fabric color laid under his chin, the way a consultant drapes cloth. Only the clothing area changes; his face, beard and skin are never edited, so what he sees is his real face next to each color.

```bash
python scripts/make_drapes.py --photo face.jpg --out drapes/ \
  --colors "Navy:#1C2541" "Optic white:#FAFAFA" "Burgundy:#6B1F2E" "Camel:#C19A6B" "Olive:#6B6B3A" \
  --metals silver gold
```

- **Pick 6–9 colors in three tiers:** 3 best, 2–3 good, 2–3 to avoid, plus the colors that decide between his season and the runner-up (or an earlier result).
- **Add metals:** `--metals silver gold` (plus `rose-gold`, `gunmetal`, `platinum`, `white-gold` or `brass` when it's close). Gold vs. silver is the classic undertone check, and it decides his watch, buckles, glasses frames and jewelry. Silver, platinum and white gold are one cool family; the choice within it is about brightness: bright and polished (white gold, polished silver) for high contrast, soft and grey (platinum, brushed silver, gunmetal) for medium or low contrast.
- **Check `_drapes_sheet.jpg`** before using the images: the fabric should start at the collar and stay off the beard and chin. If it doesn't, pass `--face x0,y0,x1,y1` (forehead to chin, fractions of the photo).
- **Say what each color does,** one line each: skin (even, red, sallow, grey), eyes, beard and jaw contours, overall impression. Compare them in pairs (navy vs. camel, optic white vs. ecru).
- **Hand him the judgment:** look at the face, not the fabric; the color that makes the face look clearer, calmer and more awake wins. A screen and one photo can mislead, so suggest confirming the two closest calls in daylight at a window with two real sweaters.

## Applying it to what he owns

If he lists clothes (text only), sort their colors into:
- **Near the face** — in palette
- **Lower body only** — off-palette but fine for trousers and shoes
- **With a buffer** — off-palette top made wearable with a good-color collar, scarf or layer between it and the face

Suggest new colors to buy only if he explicitly asks.

## Output

Findings table with confidence → palette tables → avoid list → drape images with one-line effects (when there's a photo) → combinations. Offer to save the result to `STYLE-PROFILE.md` (`mens-style-profile`) and, if he wants something to keep or share, a document in the design of `mens-style-book/references/design.md`.
