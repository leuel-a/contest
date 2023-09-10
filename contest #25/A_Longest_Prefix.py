#!/usr/bin/python3
"""Contest Problem: A Longest Prefix

Status:
"""
from collections import Counter
from typing import List


def solution():
    t = int(input())

    for _ in range(t):
        a, b = map(list, input().split())

        place = 0
        for char in a:
            if char == b[place]:
                place += 1
            else:
                try:
                    seek = b.index(char, place)
                except ValueError:
                    break
                b[seek], b[place] = b[place], b[seek]
                place = seek
        print(place)


if __name__ == "__main__":
    solution()
