#!/usr/bin/env python
#-*- coding: utf-8 -*-

def avg(a, b, c):
    return (a + b + c) / 3

def mma(a, b, c):
    return max(a, b, c), min(a, b, c), avg(a, b, c)

def main():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    maxdata, mindata, average = mma(a, b, c)
    print("Maximum =", maxdata)
    print("Minimum =", mindata)
    print("Average =", average)

if __name__ == "__main__":
    main()

