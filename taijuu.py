#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Person:
    def __init__(this, name, weight):
        this.name = name
        this.weight = weight

    def eat(this, weight):
        this.weight += weight / 1000

    def diet(this, hour):
        this.weight -= hour / 100

def main():
    kim = Person("kim", 78.1)
    print(kim.name + "さんの体重は" + str(kim.weight) + "kgです。")
    kim.eat(400)
    print(kim.name + "さんの体重は" + str(kim.weight) + "kgです。")
    kim.diet(3)
    print(kim.name + "さんの体重は" + str(kim.weight) + "kgです。")

if __name__ == "__main__":
    main()

