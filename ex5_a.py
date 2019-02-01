# coding: utf-8

RATE = 0.25
print("切り捨てられた利息は %d 銭です。" %((int(input("預金額は? ")) * RATE) % 100))
