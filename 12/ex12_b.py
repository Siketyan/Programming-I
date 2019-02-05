# -*- coding: utf-8 -*-
import sys, random

HANDS = {0: "グー", 1: "チョキ", 2: "パー"}

print("じゃんけんゲーム")

user = int(input("[0:グー, 1:チョキ, 2:パー] > "))
computer = random.randint(0, 2)

if (user < 0 or user > 2):
    print("ずるいぞ")
    sys.exit()

print("あなたは %s でした。" %HANDS[user]);
print("コンピュータは %s でした。" %HANDS[computer]);

if (user == computer):
    result = "あいこ"
elif (computer - user == 1 or computer - user == -2):
    result = "あなたの勝ち"
else:
    result = "コンピュータの勝ち"

print("結果は %s です。" %result)

