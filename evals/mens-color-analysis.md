# Evals: mens-color-analysis

## 1. Good daylight photo
**Prompt:** "Do a color analysis from this photo." + front-facing daylight photo
**Expect:**
- Findings table with a confidence label for each finding
- A 12-season label plus runner-up, and the one-line caveat that seasonal analysis is a tool, not a science
- Palettes with names and hex codes; colors to avoid near the face, each with a reason
- Skin described only in color terms; no ethnicity label
- No shopping suggestions

## 2. Poor photo
**Prompt:** "What's my color type?" + photo indoors under warm artificial light
**Expect:**
- States that the light distorts color and lowers confidence
- Asks for at most one better photo (daylight, optionally white/black tops), not a series
- Still gives a provisional result marked as an estimate

## 3. Applying to own clothes
**Prompt:** "Here are my tops: beige sweater, black T-shirt, light-blue shirt, red polo. Which can I still wear?" (after an analysis)
**Expect:**
- Sorts each item into near the face / lower body only / with a buffer
- Gives a concrete buffer (e.g. collar or scarf in a palette color) instead of "get rid of it"
- Does not suggest buying replacements

## 4. Advising someone else
**Prompt:** "My colleague wants a color analysis, here's his photo."
**Expect:**
- Addresses the colleague's coloring (not the user's)
- Mentions analyzing only with his agreement, briefly, without lecturing

## 5. Colors on his face
**Prompt:** "Do a color analysis from this photo and show me how the colors look on me." + front-facing daylight photo
**Expect:**
- Makes drape images with `scripts/make_drapes.py`: the same photo with fabric colors under the chin, face unchanged
- 6–9 colors in three tiers (best, good, avoid), plus the colors that decide between the season and its runner-up
- A metals row (at least silver vs. gold) made the same way, tied to watch, buckles and frames
- Checks the drape sheet; re-runs with `--face` if a drape covers the beard or chin
- One line per color on what it does to skin, eyes and contours; tells him to judge the face, not the fabric
- Does not generate or edit his face with an image model

## 6. Earlier result differs
**Setup:** the profile says "Season: Soft Summer"; the new photo reads as Cool Winter
**Prompt:** "Do my colors again with this new photo."
**Expect:**
- Names both results instead of silently replacing the old one
- Gives a likely reason for the difference (light, photo, beard)
- Settles it with drapes of the deciding colors from both seasons and suggests a daylight check with two real tops
- Offers to record the outcome in the profile
