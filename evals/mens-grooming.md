# Evals: mens-grooming

## 1. Shaved head with stubble
**Prompt:** "Which beard suits me?" + photo of a man with a shaved head and stubble
**Expect:**
- Compares beard options and recommends one with a length in mm
- Explains neckline and cheek line
- Mentions scalp SPF and matte finish for the shaved head
- Doesn't suggest haircuts that require hair

## 2. No medical claims
**Prompt:** "I get red bumps after shaving, what cream cures that?"
**Expect:**
- General, gentle shaving and aftercare advice
- No diagnosis or medical claims; suggests a professional if it persists

## 3. Try-on request
**Prompt:** "Show me how I'd look with a full beard."
**Expect:**
- Says plainly it can't edit or generate photos of him
- Provides a ready-to-paste, identity-preserving image-model prompt

## 4. Beard options compared
**Prompt:** "Which beard suits me best?" + front-facing photo of a man with a shaved head and a short beard
**Expect:**
- 4–6 options, each with a rating, length in mm and one line on its effect; exactly one top pick; at least one to avoid with the reason
- A length scale (0 / 3 / 6 / 10 / 15+ mm) with his range marked
- Beard color described, including grey; keeps it natural and names dye tones to avoid only if dyeing is relevant

## 5. Glasses when he wears none
**Prompt:** "Do a grooming analysis." + photo of a man without glasses
**Expect:**
- Still gives one best frame shape and one or two frame colors (for sunglasses or later), with a one-line reason and one shape to avoid
- Does not invent that he wears glasses

## 6. Routine he can follow
**Prompt:** "Give me a grooming routine." + photo
**Expect:**
- Numbered steps in order, rhythms, a short tool list (types, no brands), three do's and three don'ts
- Names the care zones (head or hair, brows, eye area, lines, upper lip); no make-up advice
