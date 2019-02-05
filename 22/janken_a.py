#!/usr/bin/env python3
#-*- coding: utf-8 -*-

HANDS = ["g", "c", "p"]
STRINGS = ["グー", "チョキ", "パー"]
QUIT = ["q", "終了"]

num_hands = len(HANDS)
data = [[0 for i in range(3)] for j in range(4)]

def print_hands():
    print("> ", end = "")
    for i in range(num_hands + 1):
        if i == num_hands:
            print("%s: %s" %(QUIT[0], QUIT[1]))
            return
        print("%s: %s," %(HANDS[i], STRINGS[i]), end = " ")

def parse_hand(char):
    if char == QUIT[0]:
        return -2
    for i in range(num_hands):
        if HANDS[i] == char:
            return i
    return -1

def suggest(last):
    maximum = -1
    indices = []
    for i in range(num_hands):
        value = data[last][i]
        if value > maximum:
            maximum = value
            indices = [i]
        elif value == maximum:
            indices.append(i)
    return indices

def select(suggestion):
    from random import randint
    return suggestion[randint(0, len(suggestion) - 1)]

def win_hand(hand):
    if hand == 0:
        return num_hands - 1
    else:
        return hand - 1

def lose_hand(hand):
    if hand == num_hands - 1:
        return 0
    else:
        return hand + 1

def test(user, agent):
    if user == agent:
        return 0
    elif user == win_hand(agent):
        return 1
    else:
        return -1

def main():
    total = [0] * 3
    last = num_hands
    while True:
        suggestion = suggest(last)
        agent = win_hand(select(suggestion))
        print_hands()
        now = parse_hand(input("< "))
        if now == -2:
            print(
                "> あなたは %d勝 %d敗 %d分 でした"
                %(total[0], total[1], total[2])
            )
            return
        elif now < 0:
            print("> 不正な値です")
            continue
        data[last][now] += 1
        last = now
        print("> あなた: %s, コンピュータ: %s" %(STRINGS[now], STRINGS[agent]))
        result = test(now, agent)
        if result == 0:
            total[2] += 1
            print("> あいこ")
        elif result < 0:
            total[1] += 1
            print("> あなたの負け")
        else:
            total[0] += 1
            print("> あなたの勝ち")

if __name__ == "__main__":
    main()

