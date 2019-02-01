gender = input("いらっしゃいませ。性別は？")
volume = int(input("ご飯の量は何g？"))

print("あなたは %s性 で、ご飯の量は %dg ですね。" %(gender, volume))

if (gender == "男"):
    if (volume >= 900):
        print("やめたほうがいいんじゃない")
    else:
        print("ごゆっくり")
elif (gender == "女"):
    if (volume >= 600):
        print("無理しないほうがいいよ")
    else:
        print("ごゆっくり")
else:
    print("ごゆっくり")

