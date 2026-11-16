# Men's Style Skills

Agent skills that turn Claude (or any skills-compatible agent) into a personal men's stylist — color analysis, outfits from the clothes you already own, grooming, and a designed personal style book.

**Principles**

- **Use what you own.** No shopping lists unless you ask for them. Problems get solved with styling, combining and tailoring.
- **No photo dumps.** One face photo for color and grooming; your wardrobe as a short text list.
- **Opinions, not textbooks.** Only the principles that change the advice are written down, as guidelines with reasons. The rest is left to the AI's judgment.
- **Honest and kind.** Critique clothes, never bodies. Confidence is stated; nothing is invented.

## Installation

### Claude Code (plugin)

```bash
claude plugin marketplace add benjaminkech/mens-style-skills
claude plugin install mens-style-skills@mens-style-skills
```

### Any agent (copies editable files)

```bash
npx skills@latest add benjaminkech/mens-style-skills
```

### Claude.ai

Download a skill folder (e.g. `skills/mens-color-analysis`), zip it and upload it under **Settings → Capabilities → Skills**.

## Quick start

1. `/mens-style-profile` — set up your profile once (body, taste, wardrobe as text).
2. `/mens-style-book` — get the full analysis as a designed multi-page style book.
3. Day to day: "What should I wear tomorrow?" — `mens-style-advisor` picks from your own clothes.

## Skills

| Skill | What it does | Input |
|---|---|---|
| [`mens-style-profile`](skills/mens-style-profile/SKILL.md) | Creates and updates `STYLE-PROFILE.md`, which all other skills read. Checks your photo first and asks for a better one if light, filters or angle would distort the analysis. | Questions, text |
| [`mens-color-analysis`](skills/mens-color-analysis/SKILL.md) | Undertone, depth, contrast, 12-season type; palettes with hex codes, metals, colors to avoid; drape images that show each color under your own face; sorts the colors you own into near-face / lower-body / with-buffer. | 1 face photo in daylight |
| [`mens-style-advisor`](skills/mens-style-advisor/SKILL.md) | Wardrobe check, 10 outfits from your own clothes, outfit of the day, occasion outfits, weekly rotation, outfit check, signature look. | Profile + wardrobe as text |
| [`mens-grooming`](skills/mens-grooming/SKILL.md) | Beard options compared with ratings and mm, length scale, neckline and cheek line; haircut or shaved-head care; care zones and a numbered routine; best glasses frame, even if you wear none yet. | 1 face photo |
| [`mens-style-book`](skills/mens-style-book/SKILL.md) | Runs everything and builds your illustrated personal style guide — clear rules with ✓/✗ examples on your own photo and clothes, outfit formulas, and a one-page cheat sheet. | Profile, 1 photo, wardrobe list (optionally with item photos) |
| [`mens-travel-packing`](skills/mens-travel-packing/SKILL.md) | Packing list and travel capsule from your own clothes, for the destination's weather, dress code, trip length, laundry and luggage, with outfits and a travel-day look. | Trip details + profile or wardrobe list |

### Style principles

The skills don't re-explain menswear basics — the AI already knows dress codes, layer order and garments. They only write down the opinions that change the advice: [`style-principles.md`](skills/mens-style-advisor/references/style-principles.md) (fit before everything, few colors and one focal point, light with light, texture over pattern, smooth layering, proportions).

## Example prompts

- "Do a color analysis from this photo."
- "Here's my wardrobe: … Give me 10 outfits for the office."
- "Wedding next month, dress code 'smart casual garden party'. What do I wear from my list?"
- "Is a T-shirt under my overcoat okay?"
- "Which beard length suits a shaved head?"
- "Make my complete style book."
- "Show me how navy and camel look on my face."
- "Work trip to Ho Chi Minh City tomorrow, 12 nights. Help me pack."

## Privacy

- Only analyze photos of people who agreed to it — including when you're helping a friend or colleague.
- Photos are never stored in `STYLE-PROFILE.md`; only the results (palette, beard length, wardrobe list).
- Skin is described in color terms only. No health or body judgments.

## Limitations

- The skills can't edit or generate photos of you. For try-on images they write an identity-preserving prompt for an image model.
- Seasonal color analysis is a practical tool, not a science. A phone photo gives an estimate; daylight and a white/black comparison raise confidence.

## Testing

[`evals/`](evals/README.md) contains test prompts with the behavior each skill must show. Run them after changing a skill.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
