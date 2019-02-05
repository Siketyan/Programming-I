#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from sys import exit
from tkinter import *

class Janken:
    HANDS = ["g", "c", "p"]
    STRINGS = ["グー", "チョキ", "パー"]
    QUIT = ["q", "終了"]
    
    def __init__(self):
        self.num_hands = len(self.HANDS)
        self.data = [[0 for i in range(3)] for j in range(4)]
        self.last = self.num_hands
        self.total = [0] * 3
        self.select_next()

    def suggest(self, last):
        maximum = -1
        indices = []
        print(self.next)
        for i in range(self.num_hands):
            value = self.data[last][i]
            if value > maximum:
                maximum = value
                indices = [i]
            elif value == maximum:
                indices.append(i)
        return indices

    def select(self, suggestion):
        from random import randint
        return suggestion[randint(0, len(suggestion) - 1)]

    def win_hand(self, hand):
        if hand == 0:
            return self.num_hands - 1
        else:
            return hand - 1

    def lose_hand(self, hand):
        if hand == self.num_hands - 1:
            return 0
        else:
            return hand + 1

    def test(self, user, agent):
        if user == agent:
            return 0
        elif user == self.win_hand(agent):
            return 1
        else:
            return -1

    def select_next(self):
        suggestion = self.suggest(self.last)
        self.next = self.win_hand(self.select(suggestion))

    def play(self, hand):
        now = hand
        agent = self.next
        self.data[self.last][now] += 1
        self.last = now
        self.select_next()
        result = self.test(now, agent)
        if result == 0:
            self.total[2] += 1
        elif result < 0:
            self.total[1] += 1
        else:
            self.total[0] += 1
        return now, agent, result

class App:
    PADDING = 1

    def play(self, hand):
        user, agent, result = self.janken.play(hand)
        if result == 0:
            result_text = "あいこ"
        elif result < 0:
            result_text = "コンピュータの勝ち"
        else:
            result_text = "あなたの勝ち"
        self.label_user.configure(text = self.janken.STRINGS[user])
        self.label_agent.configure(text = self.janken.STRINGS[agent])
        self.label_result.configure(text = result_text)

    def place_label(self, text, row, column, columnspan = None):
        label = Label(self.window, text = text)
        label.grid(
            row = row,
            column = column,
            columnspan = columnspan,
            padx = self.PADDING,
            pady = self.PADDING
        )
        return label

    def place_button(self, text, command, row, column, width = None, columnspan = None, sticky = None):
        button = Button(self.window, width = width, text = text, command = command)
        button.grid(
            row = row,
            column = column,
            columnspan = columnspan,
            sticky = sticky,
            padx = self.PADDING,
            pady = self.PADDING
        )
        return button

    def place_widgets(self):
        self.place_label("じゃんけんゲーム", 0, 0, 3)
        self.place_label("あなた", 1, 0)
        self.place_label("コンピュータ", 1, 2)
        self.label_user = self.place_label("じゃんけん", 2, 0)
        self.label_agent = self.place_label("ジャンケン", 2, 2)
        self.label_result = self.place_label("対戦結果", 3, 0, 3)
        self.place_button("グー", lambda: self.play(0), 4, 0, 10)
        self.place_button("チョキ", lambda: self.play(1), 4, 1, 10)
        self.place_button("パー", lambda: self.play(2), 4, 2, 10)
        self.place_button("ばいばい", sys.exit, 5, 0, None, 3, "ew")

    def main(self):
        self.janken = Janken()
        self.window = Tk()
        self.place_widgets()
        self.window.mainloop()

if __name__ == "__main__":
    App().main()

