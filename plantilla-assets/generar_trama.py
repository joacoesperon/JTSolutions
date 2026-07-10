#!/usr/bin/env python3
"""Generador de tramas escocesas por color, a partir de la ORIGINAL de gentlecan.

Rota el tono (hue) de la trama azul original hacia el color que pidas, conservando
exactamente el tejido y el degradado (saturación y luminosidad originales). Así:
  - al pedir el azul de gentlecan -> sale idéntica a la suya
  - al pedir cualquier otro color -> mismo tejido, color del cliente

Uso:
  python3 generar_trama.py 7CBA3F            # verde de marca
  python3 generar_trama.py 1B4F8A azul       # nombre opcional para el archivo
  python3 generar_trama.py 7CBA3F verde --tint   # además ajusta luz/saturación al color
"""
import colorsys
import sys
from pathlib import Path
from PIL import Image

SRC = Path(__file__).parent / "trama-original-azul.jpg"
OUT_DIR = Path(__file__).parent


def hex_to_hsv(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hsv(r, g, b)  # h,s,v en 0..1


def dominant_hue(img):
    """Hue medio ponderado por saturación (0..1)."""
    small = img.convert("HSV").resize((80, 40))
    px = list(small.getdata())
    num = den = 0.0
    for h, s, v in px:
        num += (h / 255) * (s / 255)
        den += s / 255
    return num / den if den else 0.0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    target_hex = sys.argv[1]
    name = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith("-") else target_hex.lstrip("#")
    tint = "--tint" in sys.argv

    th, tsat, tval = hex_to_hsv(target_hex)
    img = Image.open(SRC).convert("RGB")
    hsv = img.convert("HSV")
    H, S, V = hsv.split()

    src_h = dominant_hue(img)
    offset = round((th - src_h) * 255) % 256  # rotación de tono
    H = H.point(lambda i: (i + offset) % 256)

    if tint:
        # sube la saturación hacia la del color objetivo (útil si el cliente es muy vivo)
        sat_mul = max(0.4, min(2.0, tsat / 0.55))  # 0.55 ≈ saturación media de la original
        S = S.point(lambda i: min(255, round(i * sat_mul)))

    out = Image.merge("HSV", (H, S, V)).convert("RGB")
    dst = OUT_DIR / f"trama-{name}.jpg"
    out.save(dst, quality=88)
    print(f"OK -> {dst.name}  (offset tono {offset}/255, color base #{target_hex.lstrip('#').upper()})")


if __name__ == "__main__":
    main()
