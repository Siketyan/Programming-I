#!/usr/bin/env python
#-*- coding: utf-8 -*-

from tkinter import Tk, Canvas

def readlines():
    lines = None
    try:
        stream = open("m.txt", "r")
        lines = stream.readlines()
        stream.close()
    except IOError:
        print("Couldn't open the file.")
    except EOFError:
        print("The file is corrupted.")
        stream.close()
    return lines

def main():
    window = Tk()
    canvas = Canvas(window, width = 620, height = 620)
    canvas.pack()
    lines = readlines()
    if lines == None:
        return
    for line in lines:
        points = line.split(",")
        x1 = points[0]
        y1 = points[1]
        x2 = points[2]
        y2 = points[3]
        canvas.create_line(x1, y1, x2, y2)
    window.mainloop()

if __name__ == "__main__":
    main()

