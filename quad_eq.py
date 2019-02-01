# coding: utf-8
# 2次方程式の解を求める
import math

print("2次方程式の係数を入れてください")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = math.sqrt((b * b) - (4 * a * c))
x1 = (- b + d) / (2 * a)
x2 = (- b - d) / (2 * a)

print("解は %6.2f と %6.2f です。" %(x1, x2))

