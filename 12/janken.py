# -*- coding: utf-8 -*-
import random

print("じゃんけんゲーム")

user = int(input("[0:グー, 1:チョキ, 2:パー] > "))
computer = random.randint(0, 2)

print("あなたは %d でした。" %user);
print("コンピュータは %d でした。" %computer);

if (user == computer):
    result = "あいこ"
elif (computer - user == 1 or computer - user == -2):
    result = "あなたの勝ち"
else:
    result = "コンピュータの勝ち"

print("結果は %s です。" %result)

