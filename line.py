#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tkinter

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width = 640, height = 480)
canvas.configure(bg = "#FFF")

canvas.create_line(
    320, 50,
    200, 400,
    490, 176,
    150, 176,
    440, 400,
    320, 50,
    fill = "#272727"
)

canvas.pack()
root.mainloop()

