# Evals: mens-travel-packing

## 1. Work trip from his own wardrobe
**Setup:** a `STYLE-PROFILE.md` with palette and wardrobe exists
**Prompt:** "I fly to Ho Chi Minh City tomorrow for 12 nights, smart casual office, checked bag. Help me pack."
**Expect:**
- Asks nothing the prompt or profile already answers (at most: laundry)
- Looks up the weather for those dates and states the range
- Packs only items from his wardrobe, counted by laundry cycle (about 5 days of tops), on one color base from his palette
- A travel-day outfit that works for both departure and arrival weather; bulky pieces worn, not packed
- Flags entry rules for the trip's purpose and his passport, with the source, as something to check today
- Ends with 4–6 outfit formulas and a short "leave at home" list

## 2. Carry-on only, cold destination
**Prompt:** "Weekend in Oslo in January, carry-on only, dinner on Saturday. What do I bring?" + text wardrobe list
**Expect:**
- Layers that stack (base, knit, coat), the coat worn on the plane
- One outfit covers the dinner; everything else is one step less formal
- Two pairs of shoes at most, one worn

## 3. No shopping by default
**Prompt:** "Beach holiday in Mallorca, 7 nights." + a wardrobe list with no shorts or swimwear
**Expect:**
- Builds the list from what he owns
- Names the missing essentials (swim shorts) once, separately, without a shopping list
