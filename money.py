# -*- coding: utf-8 -*-

kodukai = int(input("基本額は? "))
result = input("成績は? ").upper()

if (result == "A"):
    kodukai *= 3
elif (result == "B"):
    kodukai *= 2
elif (result == "F"):
    kodukai //= 2
elif (result != "C"):
    print("入力エラー")
    kodukai = -1

if (kodukai > 0):
    print("今月のあなたの成績は %s ですね。" %result)
    print("従っておこづかいは %d 円です。" %kodukai)

