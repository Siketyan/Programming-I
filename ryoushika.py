# coding: utf-8

data = int(input("データ入力 "))
print("%d を量子化すると %d になります。" %(data, int((data / 10) + 0.5) * 10))
