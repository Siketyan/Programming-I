# -*- coding: utf-8 -*-

eng = input("英語の成績を入れて ")
math = input("数学の成績を入れて ")
print("あなたの成績は英語が %s で、数学が %s だね。" %(eng, math))

if ((eng == "a") | (eng == "b")) & ((math == "a") | (math == "b")):
    print("がんばったね。")
