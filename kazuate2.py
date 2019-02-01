#!/usr/bin/env python
#-*- coding: utf-8 -*-

DIGITS = 3

def generate():
    import random
    digits = [i for i in range(10)]
    return [digits.pop(random.randint(0, 9 - i)) for i in range(DIGITS)]

def split(string):
    return [int(string[i]) for i in range(DIGITS)]

def compare(num1, num2):
    hits = 0
    blows = 0
    for i in range(DIGITS):
        if num1[i] == num2[i]:
            hits += 1
            continue
        if num1[i] in num2:
            blows += 1
    return hits, blows

def main():
    number = generate()
    count = 0
    #print("#Debug:" + str(number))
    while True:
        string = input("数を入れて ")
        hits, blows = compare(number, split(string))
        count += 1
        print("%s は %d ヒット %d ブローです。" %(string, hits, blows))
        if hits == DIGITS:
            print("%d 回目で正解しました。おめでとう！！" %count)
            return

if __name__ == "__main__":
    main()

