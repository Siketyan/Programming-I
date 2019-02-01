# -*- coding: utf-8 -*-

def syahen(x, y):
    from math import sqrt
    return sqrt(x * x + y * y)

def main():
    print("直角をはさむ2辺の長さは?")
    x = float(input("x = "))
    y = float(input("y = "))
    print("斜辺の長さは %6.2f" %syahen(x, y))

if __name__ == "__main__":
    main()

