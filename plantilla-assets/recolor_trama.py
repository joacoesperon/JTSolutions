#!/usr/bin/env python3
"""Recolorea la trama escocesa de gentlecan (azul) a nuestro verde de marca.

Toma el patrón/relieve (luminancia) del JPG original y lo re-mapea a un degradado
verde: sombras -> verde oscuro, luces -> verde marca. Mismo tejido, nuestro color.
"""
from PIL import Image

SRC = "/tmp/claude-1000/-home-jesperon-JTSolutions/83eab51f-2742-4326-be0f-b8c9bea1efb6/scratchpad/textura.jpg"
DST = "/home/jesperon/JTSolutions/plantilla-assets/trama-verde.jpg"

# extremos del degradado (sombra -> luz), afinados alrededor de #7CBA3F
DARK = (30, 54, 15)      # #1E360F  sombras del tejido
LIGHT = (124, 186, 63)   # #7CBA3F  verde de marca (zonas claras)

img = Image.open(SRC).convert("L")  # luminancia = patrón del tartán

# LUT por canal: interpola DARK->LIGHT según el valor de gris
lut_r = [round(DARK[0] + (LIGHT[0] - DARK[0]) * i / 255) for i in range(256)]
lut_g = [round(DARK[1] + (LIGHT[1] - DARK[1]) * i / 255) for i in range(256)]
lut_b = [round(DARK[2] + (LIGHT[2] - DARK[2]) * i / 255) for i in range(256)]

r = img.point(lut_r)
g = img.point(lut_g)
b = img.point(lut_b)
out = Image.merge("RGB", (r, g, b))
out.save(DST, quality=88)
print("OK ->", DST, out.size)
