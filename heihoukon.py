# -*- coding: utf-8 -*-
from math import sqrt
from timeit import timeit

n = int(input("1からnまでの平方根を求めます。 n=? "))

def loop():
    i = 1
    while i <= n:
        print("%3d: %8.4f" %(i, sqrt(i)))
        i += 1

if __name__ == "__main__":
    #result = timeit("loop()", setup = "from __main__ import loop", number = 3)
    #print("while: %f" %result_while)
    loop()

