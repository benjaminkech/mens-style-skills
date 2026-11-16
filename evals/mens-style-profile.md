# Evals: mens-style-profile

## 1. New profile
**Prompt:** "Set up my style profile."
**Expect:**
- Asks only for missing information, compactly
- Produces `STYLE-PROFILE.md` in the documented format, under ~80 lines
- Marks color/grooming as "not yet analyzed" unless he agrees to run them

## 2. Privacy
**Prompt:** "Save my photo in the profile too."
**Expect:**
- Declines to store photos or photo links; stores only the analysis results
- Explains briefly

## 3. Update
**Setup:** an existing profile
**Prompt:** "I bought a grey flannel blazer and gave away my red polo."
**Expect:**
- Updates only the wardrobe section and the date

## 4. Photo check: good photo
**Prompt:** "Set up my profile, here's a photo." + front-facing daylight selfie, no filter
**Expect:**
- States a short verdict (good) before any analysis
- Offers to run color and grooming on it; records only the verdict in the profile, not the photo

## 5. Photo check: not usable
**Prompt:** "Here's my photo for the profile." + photo under warm indoor light with sunglasses
**Expect:**
- Does not run a color analysis
- Explains the problem in one or two sentences (light distorts color, sunglasses hide the eyes)
- Asks for exactly one new photo with concrete tips (window light, no flash/filter, face fills half the frame, no sunglasses)

## 6. Photo check: second photo still bad
**Setup:** the user already sent one unusable photo and was asked for another
**Prompt:** second photo, still with mixed artificial light
**Expect:**
- Does not ask a third time
- Gives results marked as estimates and suggests checking them in a mirror in daylight

## 7. Beginner-friendly setup
**Prompt:** "hallo, ein kollege hat mir das geschickt. was muss ich machen?"
**Expect:**
- Friendly short intro, then at most 2–3 questions with example answers and a progress hint
- No jargon in what the user reads (no file names, Markdown, "skill", "dataset")
- Says that skipping is fine; photo and wardrobe offered as optional, not demanded

## 8. Saving in a normal chat
**Setup:** Claude.ai or ChatGPT chat without a persistent folder
**Prompt:** answers to all setup questions
**Expect:**
- Gives the profile as one short text block
- Explains in 1–2 sentences how to keep it (project note/file, or paste next time)
- Ends with exactly three concrete next steps
