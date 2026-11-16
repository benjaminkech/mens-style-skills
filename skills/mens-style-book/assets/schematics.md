# Schematic drawings: beard options and frame shapes

Simple line drawings for comparing **options** (beard styles, frame shapes) side by side. They are deliberately generic: a neutral head outline, not him. Label them as schematic, never present them as his face, and keep his real face for the drape, beard close-up and zone map pages.

Paste the SVG inline. Style with two classes (or inline attributes): `.hd` for the head outline (`fill: none; stroke: #6B675F; stroke-width: 1.6`) and `.hr` for hair or frame (`fill: #3A3530` for beards; frames use `fill: none; stroke: #1F1F1F; stroke-width: 2.2`). Change `.hr` fill to match his beard color.

## Beard options (viewBox 0 0 120 160)

Shared head outline, used in every beard drawing:

```svg
<ellipse class="hd" cx="60" cy="58" rx="27" ry="35"/>
<path class="hd" d="M50 92v12M70 92v12M16 156Q60 112 104 156"/>
<path class="hd" d="M33 54q-6 2-4 10q2 4 5 2M87 54q6 2 4 10q-2 4-5 2"/>
```

Add one of these beard shapes after the outline:

| Option | Shape |
|---|---|
| Clean shaven (with moustache hint off) | *(outline only)* |
| Stubble, ~3 mm | `<path class="hr" style="opacity:0.55" d="M34 62Q36 94 60 96Q84 94 86 62Q78 80 60 82Q42 80 34 62Z"/>` |
| Short boxed beard, ~5–7 mm | `<path class="hr" d="M33 58L35 92Q60 102 85 92L87 58Q78 84 60 84Q42 84 33 58Z"/><path class="hr" d="M48 74Q60 70 72 74Q60 79 48 74Z"/>` |
| Fade beard | `<path class="hr" d="M33 58Q34 66 38 74Q44 100 60 102Q76 100 82 74Q86 66 87 58Q78 80 60 80Q42 80 33 58Z"/><path class="hr" d="M48 74Q60 70 72 74Q60 79 48 74Z"/>` |
| Short full beard, ~10 mm | `<path class="hr" d="M32 56Q30 96 60 112Q90 96 88 56Q78 82 60 82Q42 82 32 56Z"/><path class="hr" d="M48 74Q60 70 72 74Q60 79 48 74Z"/>` |
| Long full beard, 15 mm+ | `<path class="hr" d="M31 55Q27 104 60 130Q93 104 89 55Q78 82 60 82Q42 82 31 55Z"/><path class="hr" d="M48 74Q60 70 72 74Q60 79 48 74Z"/>` |

Under each drawing: the rating (top pick / very good / good / avoid), the name, the length in mm, and one line on what it does.

## Frame shapes (viewBox 0 0 120 48)

| Shape | Drawing |
|---|---|
| Rectangular, rounded corners | `<rect class="hr" x="8" y="12" width="44" height="26" rx="8"/><rect class="hr" x="68" y="12" width="44" height="26" rx="8"/><path class="hr" d="M52 22q8-5 16 0"/>` |
| Panto (soft round) | `<path class="hr" d="M10 16q20-6 40 0q4 16-6 22q-14 6-28 0q-10-6-6-22z"/><path class="hr" d="M70 16q20-6 40 0q4 16-6 22q-14 6-28 0q-10-6-6-22z"/><path class="hr" d="M50 20q10-5 20 0"/>` |
| Browline | `<path class="hr" style="stroke-width:5" d="M8 14h44M68 14h44"/><path class="hr" d="M10 14q-2 20 18 22q22 0 22-22M70 14q0 22 22 22q20-2 18-22"/><path class="hr" d="M52 18q8-5 16 0"/>` |
| Aviator | `<path class="hr" d="M8 12h44q2 18-10 26q-14 6-26-4q-10-10-8-22z"/><path class="hr" d="M68 12h44q2 12-8 22q-12 10-26 4q-12-8-10-26z"/><path class="hr" d="M52 14h16M52 20q8-4 16 0"/>` |

Show 2–3 shapes in a row: his best shape marked ✓ with one or two frame-color swatches beside it, one shape to avoid marked ✗.
