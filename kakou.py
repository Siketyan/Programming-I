#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PIL import Image

warai = Image.open("warai_b.png")
warai = warai.resize((int(warai.size[0] / 3.5), int(warai.size[1] // 3.5)))

lenna = Image.open("Lenna.jpg")
lenna.paste(warai, (160, 180), warai)
lenna.show()

