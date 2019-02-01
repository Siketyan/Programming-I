# -*- coding: utf-8 -*-

vehicle = {
    "m": "メリーゴーランド",
    "j": "ジェットコースタ"
}

age = int(input("年齢は？ "))
choice = input("メリーゴーランド: m, ジェットコースター: j\n乗りたいものは？ (m or j) ")

print("あなたの年齢は %d 歳で、希望の乗り物は %s ですね。" %(age, vehicle[choice]))
if ((choice == "m") & (age >= 5)) | ((choice == "j") & (age >= 8)):
    print("どうぞお乗りください")
else:
    print("大きくなってからね")

