---
name: mens-style-book
description: Use when a man wants his complete personal style book, style guide, style booklet or makeover document — color analysis, grooming, wardrobe check and outfits combined into one illustrated, practical guide with his photo, his own clothes, clear rules and do/don't examples, plus a one-page cheat sheet. Also use to restyle or update an existing style book.
---

# Men's Style Book

Run the whole collection end to end and deliver one **Personal Style Guide**: an illustrated, practical booklet about him in the spirit of a good style coach's how-to guides. Clear rules, one-sentence reasons, pictures of him and his own clothes, ✓/✗ examples, and a cheat sheet at the end. Answer and write the pages in the user's language. The user may be making this for someone else: address that person, and only use photos he agreed to.

**Read `references/design.md` before building any page.** It defines the rule → why → picture → ✓/✗ pattern and the page recipes. He should be able to apply every page the next morning: a report full of tables fails, and so does an over-styled magazine. The test for each page: does it teach a few rules and show them on his face or his clothes?

## Flow

1. **Profile.** Read `STYLE-PROFILE.md` if it exists. Otherwise gather the basics as `mens-style-profile` describes, and offer to save the profile at the end.
2. **Inputs.** At most one or two face photos, plus the wardrobe as a text list or a dataset (e.g. a spreadsheet with item photos). Check the photo with `mens-style-profile/references/photo-check.md` before anything else, and ask for one better photo if it isn't usable.
3. **Analyses**, each following its skill:
   - Color → `mens-color-analysis`
   - Beard, head/hair, skin, glasses → `mens-grooming`
   - Wardrobe check, outfits, signature look → `mens-style-advisor`
   Reuse results already in the conversation, project or profile instead of redoing them.
4. **Images.** Prepare them before building pages (see below).
5. **Pages.** Build them one at a time in the design from `references/design.md`, and share each one when it's done. If he asks to go page by page ("make page 1"), make only that page and wait.
6. **Close.** Offer to save or update `STYLE-PROFILE.md` with the results.

## Pages

| # | Page | Content |
|---|---|---|
| 0 | Cover and contents | Title, name, date, his photo in a calm frame, contents, key result in one line |
| 1 | Your colors | His color profile at a glance (season, undertone, contrast / depth / brightness meters), palette as swatch rows, colors to avoid, metals and white |
| 2 | Your colors on you | Drape images of his own face: best, good and avoid colors, then a metals row (silver vs. gold and the closest call), each with what it does to skin, eyes and contours |
| 3 | Applying color | Do/don't with his own items, wearing off-palette pieces with a buffer, color formulas |
| 4 | Grooming | Zone map on his photo (head, brows, eye area, lines, upper lip), numbered routine, rhythms, tools, do's and don'ts |
| 5 | Your best beard | Beard options as schematic cards with ratings and mm (one top pick, one to avoid), length scale with his range marked, annotated close-up of his beard with the lines, beard color |
| 6 | Head or hair & glasses | Shaved-head care, or cuts and barber words; his current frame verdict, or his best frame shape and colors even if he wears none |
| 7 | Wardrobe | His basics as a product row, near face / with buffer / lower body, what he doesn't need, 10 outfit formulas |
| 8 | Your best look | Cheat sheet: "Your 10 rules", palette row, metals, two signature outfits with images, beard, glasses, best fabrics and necklines, his look in 3–5 words |

Every page ends with a short "Your rules" box. Merge or drop pages that lack material, but keep the cheat sheet. With no photo, pages 2 and 4's zone map are dropped and the beard page keeps only the schematic cards. With no wardrobe list, page 7 becomes a short "send me your wardrobe" note and outfits use color chips. No shopping list unless he asked for one.

## Images

Images are what make the book feel personal and easy to picture, so use them wherever he has provided material:

- **His photo** (only with his consent, after the photo check): one photo, cropped into a portrait, a beard close-up and an eye-line crop.
- **His colors on him:** drape images from the same photo, colors and metals, made with `mens-color-analysis/scripts/make_drapes.py` (see that skill's drape test). This is the page people remember, because they see their own face change.
- **Options, not him:** beard styles and frame shapes are compared with the schematic drawings in `assets/schematics.md`. They are generic outlines, labeled as schematic; his real face stays on the drape, zone map and close-up.
- **His clothes:** if his wardrobe comes with item photos, use 6–8 key items for the basics row, 3–4 per outfit formula, and his own off-palette items for the ✗ examples.

Prepare them with the bundled script. It converts any format to JPG, resizes the images, makes the three face crops, and builds a contact sheet so you can check the result:

```bash
python scripts/prepare_images.py --photo face.jpg --items item1.avif item2.webp ... --out images/
```

The face crops follow the detected face (OpenCV, if installed). Look at `images/_contact_sheet.jpg` before using the images. Drop any product photo with baked-in text; crop away or drop any that shows a model's face. If a face crop misses, pass `--face x0,y0,x1,y1` (forehead to chin), or fix a single crop with `--crop-portrait`, `--crop-beard` or `--crop-eyes` (fractions of the photo). JPEG XL (.jxl) photos need `pip install pillow-jxl-plugin`; the script names any file it can't read.

Never stand in for him or his clothes with stock photos, illustrations or AI-generated images. If he wants try-on images (other beards, cuts, outfits), add an appendix with ready-to-paste, identity-preserving prompts for an image model.

Keep his photos and shop product photos in his private document only.

## Page size

Size each page to its content. If the environment can't preview pages (some design canvases forbid it), estimate generously: empty space at the bottom of a page is better than cut-off rules.
