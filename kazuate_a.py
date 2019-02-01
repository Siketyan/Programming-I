from random import randint

count = 0
num = randint(1, 100)
while True:
    i = int(input("数を当ててみて"))
    count += 1

    if i < num:
        print("もっと大きいよ。")
        continue

    if i > num:
        print("もっと小さいよ。")
        continue

    print("正解です。おめでとう。 (%d 回目)" %count)
    break

