# Evals: mens-style-advisor

## 1. No shopping by default
**Prompt:** "Give me 10 office outfits." + text wardrobe list (8–12 items)
**Expect:**
- Uses only items from the list
- No purchase suggestions, no "consider adding…"
- One-line formulas, labeled by occasion

## 2. No wardrobe photos
**Prompt:** "Help me with my wardrobe."
**Expect:**
- Offers a text template for the wardrobe list
- Does not ask for photos of clothes

## 3. Explicit gaps
**Prompt:** "What should I buy next?" (with a wardrobe list)
**Expect:**
- At most 3 items, each with why it unlocks new outfits from what he owns

## 4. Judgment over rigid rules
**Prompt:** "Can I wear a crewneck sweater over my oxford shirt to the office?"
**Expect:**
- Answers by context (fine for smart casual if the collar sits well; a V-neck reads more formal with a tie)
- Does not state an absolute rule

## 5. Proportions
**Prompt:** "I'm 165 cm with short legs. How should my trousers fit?"
**Expect:**
- Higher rise, no break, tonal lower half; reason given in one clause each
- No comments that judge his body

## 6. Uses the profile
**Setup:** a `STYLE-PROFILE.md` with palette and wardrobe exists
**Prompt:** "What should I wear tomorrow? Client meeting, 5 °C."
**Expect:**
- Doesn't re-ask questions the profile answers
- Picks face-near colors from the profile's palette
