# coding: utf-8
from math import *

points = ["A", "B", "C"]
p = [[0] * 2, [0] * 2, [0] * 2]

for i in range(3):
    p[i][0] = int(input("x%d = " %(i + 1)))
    p[i][1] = int(input("y%d = " %(i + 1)))

print("p =", p)

for i in range(3):
    print("%s =" %points[i], p[i])

s = (1 / 2) * abs(((p[1][0] - p[0][0]) * (p[2][1] - p[0][1])) - ((p[1][1] - p[0][1]) * (p[2][0] - p[0][0])))
print("S =", s)

