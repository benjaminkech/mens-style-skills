#!/usr/bin/env python3
"""Prepare images for a men's style book.

- Converts item photos (jpg, png, webp, avif, heic*, jxl*) to RGB JPG on white, max 900 px.
- Crops one face photo into portrait, beard close-up and eye-line (glasses) banner.
- Writes a contact sheet to check everything at a glance.

* heic/jxl need the matching Pillow plugin: pip install pillow-heif / pillow-jxl-plugin.
  Unreadable files are reported and skipped.

Face crops follow the face: detected with OpenCV if installed, or given with --face
(forehead to chin, fractions x0,y0,x1,y1). Without either, fixed defaults for a
typical selfie are used; check the contact sheet.

Usage:
  python prepare_images.py --photo face.jpg --items a.avif b.webp --out images/
  python prepare_images.py --photo face.jpg --face 0.31,0.30,0.73,0.75 --out images/
  python prepare_images.py --photo face.jpg --crop-beard 0.1,0.3,0.65,0.62 --out images/
"""
import argparse
import os
import re
import sys

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is required: pip install pillow")

for plugin in ("pillow_heif", "pillow_jxl"):
    try:
        mod = __import__(plugin)
        if plugin == "pillow_heif":
            mod.register_heif_opener()
    except Exception:
        pass

# Where the face (forehead to chin) usually sits in a front-facing phone selfie, as fractions.
DEFAULT_FACE = (0.30, 0.28, 0.72, 0.74)
SIZES = {"portrait": None, "beard": (640, 680), "eyes": (740, 360)}


def detect_face(im):
    """Largest face as fractions (x0, y0, x1, y1), forehead to chin, or None."""
    try:
        import cv2
        import numpy as np
        g = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2GRAY)
        s = min(1.0, 900 / max(g.shape))
        g = cv2.resize(g, None, fx=s, fy=s) if s < 1 else g
        casc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        if casc.empty():
            return None
        faces = casc.detectMultiScale(g, scaleFactor=1.1, minNeighbors=6, minSize=(80, 80))
    except Exception:
        return None
    if len(faces) == 0:
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    H, W = g.shape
    # Haar boxes end near the mouth; extend to the chin (and a short beard).
    return (x / W, y / H, (x + w) / W, min(1.0, (y + h * 1.18) / H))


def crops_from_face(face, W, H):
    """Portrait, beard and eye-line boxes (fractions) derived from a face box."""
    fx0, fy0, fx1, fy1 = face
    fw, fh = fx1 - fx0, fy1 - fy0
    cx = (fx0 + fx1) / 2
    top, bottom = max(0.0, fy0 - 0.36 * fh), min(1.0, fy1 + 0.15 * fh)
    half_w = (bottom - top) * H * 0.85 / 2 / W
    clamp = lambda v: max(0.0, min(1.0, v))
    return {
        "portrait": (clamp(cx - half_w), top, clamp(cx + half_w), bottom),
        "beard": (clamp(cx - 0.58 * fw), clamp(fy0 + 0.36 * fh), clamp(cx + 0.58 * fw), clamp(fy1 + 0.05 * fh)),
        "eyes": (clamp(cx - 0.60 * fw), clamp(fy0 + 0.07 * fh), clamp(cx + 0.60 * fw), clamp(fy0 + 0.40 * fh)),
    }


def load_rgb(path):
    im = ImageOps.exif_transpose(Image.open(path))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def slug(path):
    base = os.path.basename(path)
    base = re.sub(r"(\.[A-Za-z0-9]+)+$", "", base)
    return re.sub(r"[^A-Za-z0-9_-]+", "-", base).strip("-").lower() or "item"


def parse_box(s):
    vals = [float(v) for v in s.split(",")]
    if len(vals) != 4 or not all(0 <= v <= 1 for v in vals) or vals[0] >= vals[2] or vals[1] >= vals[3]:
        raise argparse.ArgumentTypeError("crop must be x0,y0,x1,y1 as fractions 0-1 with x0<x1, y0<y1")
    return tuple(vals)


def crop(im, box, size=None):
    w, h = im.size
    c = im.crop((int(box[0] * w), int(box[1] * h), int(box[2] * w), int(box[3] * h)))
    if size:
        c = ImageOps.fit(c, size, Image.LANCZOS)
    else:
        c.thumbnail((1200, 1200))
    return c


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--photo", help="front-facing face photo (with consent)")
    ap.add_argument("--items", nargs="*", default=[], help="item/product photos of his own clothes")
    ap.add_argument("--out", required=True, help="output folder")
    ap.add_argument("--face", type=parse_box, help="face box x0,y0,x1,y1 (forehead to chin), overrides detection")
    ap.add_argument("--crop-portrait", type=parse_box)
    ap.add_argument("--crop-beard", type=parse_box)
    ap.add_argument("--crop-eyes", type=parse_box)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    made = []

    if a.photo:
        face = load_rgb(a.photo)
        fbox = a.face or detect_face(face)
        if fbox:
            base = crops_from_face(fbox, *face.size)
            print(("face box (given): " if a.face else "face box (detected): ") + ",".join(f"{v:.2f}" for v in fbox))
        else:
            base = crops_from_face(DEFAULT_FACE, *face.size)
            print("no face box: using a typical-selfie guess - check the contact sheet, pass --face if they miss")
        boxes = {
            "portrait": a.crop_portrait or base["portrait"],
            "beard": a.crop_beard or base["beard"],
            "eyes": a.crop_eyes or base["eyes"],
        }
        for name, box in boxes.items():
            p = os.path.join(a.out, f"{name}.jpg")
            crop(face, box, SIZES[name]).save(p, quality=88)
            made.append(p)

    for path in a.items:
        try:
            im = load_rgb(path)
        except Exception as e:
            hint = " - pip install pillow-jxl-plugin" if path.lower().endswith(".jxl") else (" - pip install pillow-heif" if path.lower().endswith((".heic", ".heif")) else "")
            print(f"skipped (unreadable): {path} ({e.__class__.__name__}){hint}", file=sys.stderr)
            continue
        im.thumbnail((900, 900))
        p = os.path.join(a.out, f"{slug(path)}.jpg")
        n = 2
        while p in made:
            p = os.path.join(a.out, f"{slug(path)}-{n}.jpg")
            n += 1
        im.save(p, quality=85)
        made.append(p)

    if made:
        cell, cols = 220, 6
        rows = (len(made) + cols - 1) // cols
        sheet = Image.new("RGB", (cell * cols, (cell + 20) * rows), "white")
        for i, p in enumerate(made):
            t = Image.open(p)
            t.thumbnail((cell - 10, cell - 10))
            sheet.paste(t, ((i % cols) * cell + 5, (i // cols) * (cell + 20) + 5))
        sheet_path = os.path.join(a.out, "_contact_sheet.jpg")
        sheet.save(sheet_path, quality=80)
        print("contact sheet:", sheet_path)

    for p in made:
        print(p)


if __name__ == "__main__":
    main()
