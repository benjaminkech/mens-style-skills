# Evals: mens-style-book

## 1. Full book
**Prompt:** "Make my complete style book." + one face photo + text wardrobe list
**Expect:**
- Up to 6 pages in the documented design (cream, dark green, serif headings, swatches with hex codes)
- Pages built one after another, not one giant output
- Reuses existing results instead of redoing analyses
- No shopping list unless asked

## 2. Page by page
**Prompt:** "Make page 1."
**Expect:**
- Only page 1, then waits

## 3. No fake images
**Prompt:** "Put pictures of me with different beards on page 3."
**Expect:**
- Doesn't generate or use stock images of other people as if they were him
- Offers identity-preserving image-model prompts in an appendix

## 4. Style-guide look
**Prompt:** "Make my complete style book." + face photo + wardrobe list with item photos
**Expect:**
- Pages are built from rule blocks: instruction headline, one or two sentences of why, a picture, ✓/✗ captions
- Do/don't examples use his own items or his photo (e.g. a navy sweater ✓ vs. his black turtleneck alone ✗)
- Every page ends with a short "Deine Regeln" checklist; the last page is a one-page cheat sheet
- No magazine theatrics (no full-bleed cover portrait, no giant display type) and no table-heavy report pages
- At most ~120 words of running text per page

## 5. Images prepared, not improvised
**Prompt:** same as 4, with item photos in .avif/.webp/.jxl
**Expect:**
- Uses `scripts/prepare_images.py` (or equivalent) to convert to JPG and crop the face photo
- Checks the contact sheet and drops unusable images; unreadable formats are reported, not silently broken

## 6. Colors on him
**Prompt:** "Make my complete style book." + one face photo
**Expect:**
- Includes a "Your colors on you" page with drape rows of his own photo: best colors ✓ and colors to avoid ✗, all at the same crop and size
- One effect line per drape (skin, eyes, contours); no face edited or generated
- Without a photo, the page is left out rather than faked with swatches

## 7. Beard, glasses and best look
**Prompt:** "Make my complete style book." + one face photo of a man without glasses
**Expect:**
- A beard page with schematic option cards (rating, mm, effect), one top pick, a length scale and an annotated close-up of his own beard
- A grooming page with a zone map on his photo and numbered routine steps
- A glasses section with his best frame shape and colors even though he wears none
- The last page summarizes his best look: rules, palette, metals, two outfits, beard, glasses, fabrics and necklines, 3–5 words
- Schematic drawings are labeled as such; nothing pretends to be his face
