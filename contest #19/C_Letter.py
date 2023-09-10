#!/usr/bin/python3
""""""
from typing import List


def solution():
    _str = list(input())

    write = 0
    for read in range(len(_str)):
        while write <= read and _str[write].isupper():
            write += 1


if __name__ == '__main__':
    solution()
