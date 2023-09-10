#!/usr/bin/python3
""""""
from typing import List


def main():
    t = int(input())

    for _ in range(t):
        a = list(input())

        # Max jump he can make is the entire len of a
        i = 1
        j = len(a)
