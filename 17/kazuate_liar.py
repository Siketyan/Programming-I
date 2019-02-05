from random import randint

count = 0
num = randint(1, 100)
while True:
    i = int(input("数を当ててみて"))
    if i < 1 or i > 100:
        print("不正な入力です。数値の書式と範囲を確認し、再試行してください。")
        continue

    count += 1
    liar = randint(0, 4) == 0

    if (liar and i > num) or i < num:
        print("もっと大きいよ。")
        continue

    if (liar and i < num) or i > num:
        print("もっと小さいよ。")
        continue

    print("正解です。おめでとう。 (%d 回目)" %count)
    break

