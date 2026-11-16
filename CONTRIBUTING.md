# Contributing

Thanks for helping make better men's style advice available to everyone.

## Structure

```
skills/<skill-name>/SKILL.md          # the skill: frontmatter (name, description) + instructions
skills/<skill-name>/references/*.md   # rule files the skill reads when relevant
```

- `name` in the frontmatter matches the folder name, kebab-case.
- `description` is one line saying **when** to use the skill — it decides when the agent loads it.
- Keep `SKILL.md` focused; move detailed rule sets into `references/` and point to them from `SKILL.md`.

## Writing guidelines

- **Only what changes the advice:** don't document general menswear knowledge the AI already has (what a dress code means, what a blazer is). Write down opinions, defaults and constraints.

- **Guidelines, not hard rules:** write each guideline with its *why*, so the agent can judge when it applies and explain when breaking it looks better. Avoid absolute "never/only" rules.
- **Concrete:** name what to look for (weight, formality, depth, focal point), not just "looks nice".
- **Own words:** don't paste text or images from books, paid courses, apps or websites. Summarize the idea in your own words.
- **No shopping bias:** prefer solutions with existing clothes and tailoring; no affiliate links or brand promotion.
- **Respectful:** advice is about clothes and grooming, never about judging bodies. Describe skin only in color terms.

## Pull requests

1. One topic per PR (a new skill, a new reference, or a rule change).
2. Explain what changes in the agent's advice and give one example prompt.
3. Add or update evals in `evals/` and run them; add a `CHANGELOG.md` entry and bump the version in `.claude-plugin/plugin.json`.
4. Never commit photos of real people.
3. If a rule changes behavior across skills (e.g. color counts), update the other skills' references too.
