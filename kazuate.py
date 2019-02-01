from random import randint

num = randint(1, 100)
while True:
    i = int(input("数を当ててみて"))

    if i < num:
        print("もっと大きいよ。")
        continue

    if i > num:
        print("もっと小さいよ。")
        continue

    print("正解です。おめでとう。")
    break

