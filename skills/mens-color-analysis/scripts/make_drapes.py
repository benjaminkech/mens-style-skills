#!/usr/bin/env python3
"""Color drapes: show colors next to HIS face without changing the face.

Lays a flat "fabric" of each color over the clothing area below his chin, the
way a color consultant drapes cloth under the face. Only the clothing area is
recolored; face, beard, neck and skin pixels are never altered.

Metals work the same way (the classic gold-vs-silver drape): a brushed-metal fabric
with sheen instead of a flat color.

Usage:
  python make_drapes.py --photo face.jpg --colors "Navy:#1C2541" "Camel:#C19A6B" --out drapes/
  python make_drapes.py --photo face.jpg --metals silver gold rose-gold gunmetal --out drapes/
  python make_drapes.py --photo face.jpg --colors ... --face 0.30,0.28,0.76,0.74 --out drapes/

Output: one portrait JPG per color (drape-<name>.jpg), plus _drapes_sheet.jpg to check placement.
The face box (fractions x0,y0,x1,y1, forehead to chin) is detected with OpenCV if available;
pass --face to override when detection misses (check the sheet).
"""
import argparse
import os
import re
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageOps
except ImportError:
    sys.exit("Pillow is required: pip install pillow")


def detect_face(im):
    """Return (x0, y0, x1, y1) in pixels of the largest face, or None."""
    try:
        import cv2
        import numpy as np
    except ImportError:
        return None
    g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
    small = 900 / max(g.shape)
    g2 = cv2.resize(g, None, fx=small, fy=small) if small < 1 else g
    s = small if small < 1 else 1
    try:
        casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        if casc.empty():
            return None
        faces = casc.detectMultiScale(g2, scaleFactor=1.1, minNeighbors=6, minSize=(80, 80))
    except Exception:
        return None
    if len(faces) == 0:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    # Haar boxes stop around the mouth/upper chin; extend down to the chin (+beard).
    return (x / s, y / s, (x + w) / s, (y + h * 1.18) / s)


def parse_box(s):
    v = [float(x) for x in s.split(",")]
    if len(v) != 4 or not all(0 <= x <= 1 for x in v) or v[0] >= v[2] or v[1] >= v[3]:
        raise argparse.ArgumentTypeError("--face must be x0,y0,x1,y1 fractions")
    return v


def parse_color(s):
    m = re.match(r"^(.+?):(#[0-9A-Fa-f]{6})$", s.strip())
    if not m:
        raise argparse.ArgumentTypeError(f"color must be Name:#RRGGBB, got {s!r}")
    return m.group(1).strip(), m.group(2)


METALS = {  # light, mid, dark tones of each metal
    "silver": ((236, 239, 242), (176, 182, 189), (110, 116, 124)),
    "platinum": ((232, 232, 230), (178, 179, 178), (118, 120, 122)),   # greyer, softer sheen
    "white-gold": ((252, 252, 250), (214, 214, 210), (150, 150, 146)), # rhodium-plated: brightest, crisp
    "gunmetal": ((150, 155, 161), (88, 93, 99), (44, 47, 51)),
    "gold": ((250, 229, 160), (212, 172, 72), (140, 100, 30)),
    "rose-gold": ((246, 214, 200), (205, 146, 124), (138, 86, 70)),
    "brass": ((230, 208, 140), (181, 151, 72), (112, 88, 36)),
}


def metal_fabric(W, H, tones, seed=7):
    """Brushed metal with a soft diagonal sheen, as an RGB image."""
    import random
    light, mid, dark = tones
    small = Image.new("RGB", (64, 64))
    px = small.load()
    for y in range(64):
        for x in range(64):
            t = (x * 0.55 + y * 0.45) / 63          # diagonal position 0..1
            # two highlight bands, like folds of lamé fabric catching the light
            band = max(0.0, 1 - abs(t - 0.32) / 0.22) ** 1.5 + 0.7 * max(0.0, 1 - abs(t - 0.75) / 0.16) ** 1.5
            base = [m + (d - m) * min(1.0, 0.25 + 0.9 * abs(t - 0.32)) for m, d in zip(mid, dark)]
            c = [b + (l - b) * min(1.0, band) for b, l in zip(base, light)]
            px[x, y] = tuple(int(v) for v in c)
    fab = small.resize((W, H), Image.BICUBIC)
    rnd = random.Random(seed)
    streaks = Image.new("L", (1, H))
    for y in range(H):
        streaks.putpixel((0, y), 128 + rnd.randint(-7, 7))
    streaks = streaks.resize((W, H)).filter(ImageFilter.GaussianBlur(0.6))
    from PIL import ImageChops
    return ImageChops.overlay(fab, Image.merge("RGB", (streaks,) * 3)) if hasattr(ImageChops, "overlay") else fab


def drape(im, face, color, scale=3):
    """Return a copy of im with a fabric of `color` (hex, or a METALS key) below the chin."""
    W, H = im.size
    fx0, fy0, fx1, fy1 = face
    fw = fx1 - fx0
    cx = (fx0 + fx1) / 2
    chin = fy1
    # Neckline: a soft U under the chin, rising onto the shoulders like draped cloth.
    neck_half = fw * 0.36            # half width of the neck opening
    dip = chin + fw * 0.22           # lowest point of the neckline (centre)
    shoulder = chin - fw * 0.10      # where the cloth meets the shoulders (covers the shirt)
    pts = [(0, H), (0, shoulder + fw * 0.12), (cx - fw * 1.0, shoulder + fw * 0.08),
           (cx - neck_half * 1.25, shoulder)]
    steps = 24
    for i in range(steps + 1):  # quadratic U from left neck edge to right neck edge
        t = i / steps
        x = (cx - neck_half * 1.25) * (1 - t) ** 2 + cx * 2 * t * (1 - t) + (cx + neck_half * 1.25) * t ** 2
        y = shoulder * (1 - t) ** 2 + (dip + fw * 0.12) * 2 * t * (1 - t) + shoulder * t ** 2
        pts.append((x, y))
    pts += [(cx + fw * 1.0, shoulder + fw * 0.08), (W, shoulder + fw * 0.12), (W, H)]

    mask = Image.new("L", (W * scale, H * scale), 0)
    ImageDraw.Draw(mask).polygon([(x * scale, y * scale) for x, y in pts], fill=255)
    mask = mask.resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))

    if color in METALS:
        fabric = metal_fabric(W, H, METALS[color])
    else:
        rgb = tuple(int(color[i:i + 2], 16) for i in (1, 3, 5))
        fabric = Image.new("RGB", (W, H), rgb)
    # A soft shadow along the top edge so it reads as cloth, not a sticker.
    shade = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shade).line(pts[3:-3], fill=90, width=max(4, int(fw * 0.05)))
    shade = shade.filter(ImageFilter.GaussianBlur(fw * 0.03))
    fabric = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), fabric, shade.point(lambda v: v * 0.35))
    out = im.copy()
    out.paste(fabric, (0, 0), mask)
    return out


def portrait_box(face, W, H):
    fx0, fy0, fx1, fy1 = face
    fw, fh = fx1 - fx0, fy1 - fy0
    cx = (fx0 + fx1) / 2
    top = max(0, fy0 - fh * 0.30)
    bottom = min(H, fy1 + fh * 0.55)
    h = bottom - top
    w = h * 0.8
    x0 = max(0, min(W - w, cx - w / 2))
    return (int(x0), int(top), int(x0 + w), int(bottom))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--photo", required=True)
    ap.add_argument("--colors", nargs="+", type=parse_color, default=[], help='"Name:#RRGGBB" ...')
    ap.add_argument("--metals", nargs="+", default=[], choices=sorted(METALS), help="metal drapes, e.g. silver gold")
    ap.add_argument("--face", type=parse_box, help="override face box x0,y0,x1,y1 (fractions)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", default="480x600", help="output size WxH (default 480x600)")
    a = ap.parse_args()
    if not a.colors and not a.metals:
        ap.error("give --colors and/or --metals")
    a.colors = list(a.colors) + [(m.replace("-", " ").title(), m) for m in a.metals]

    im = ImageOps.exif_transpose(Image.open(a.photo)).convert("RGB")
    W, H = im.size
    if a.face:
        face = (a.face[0] * W, a.face[1] * H, a.face[2] * W, a.face[3] * H)
        how = "given"
    else:
        face = detect_face(im)
        how = "detected"
        if face is None:
            face = (0.30 * W, 0.28 * H, 0.72 * W, 0.74 * H)
            how = "default guess (no detector) - check the sheet, pass --face if off"
    print(f"face box ({how}): " + ",".join(f"{v:.2f}" for v in (face[0] / W, face[1] / H, face[2] / W, face[3] / H)))

    os.makedirs(a.out, exist_ok=True)
    ow, oh = (int(v) for v in a.size.lower().split("x"))
    box = portrait_box(face, W, H)
    made = []
    for name, hexv in a.colors:
        d = drape(im, face, hexv).crop(box)
        d = ImageOps.fit(d, (ow, oh), Image.LANCZOS)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        p = os.path.join(a.out, f"drape-{slug}.jpg")
        d.save(p, quality=88)
        made.append((p, name, hexv))
        print(p)

    cols = min(4, len(made))
    tw, th = 240, 300
    rows = (len(made) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * (th + 24)), "white")
    dr = ImageDraw.Draw(sheet)
    for i, (p, name, hexv) in enumerate(made):
        t = Image.open(p).resize((tw - 8, th - 8))
        x, y = (i % cols) * tw + 4, (i // cols) * (th + 24) + 4
        sheet.paste(t, (x, y))
        dr.text((x, y + th - 4), name if hexv in METALS else f"{name} {hexv}", fill=(40, 40, 40))
    sp = os.path.join(a.out, "_drapes_sheet.jpg")
    sheet.save(sp, quality=82)
    print("sheet:", sp)


if __name__ == "__main__":
    main()
