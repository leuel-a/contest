#!/usr/bin/python3
""""""
from typing import List


def solution():
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    print(*nums)


if __name__ == '__main__':
    solution()
