#!/usr/bin/env python3
"""Contest Problem A --> String Building"""
from typing import List, Tuple, DefaultDict, Deque


def solution():
    t = int(input())
    options = set(['aa', 'aaa', 'bb', 'bbb'])

    for _ in range(t):
        s = input()
        dp = [False for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            next1, next2 = True, True
            way1, way2 = False, False
            if i + 2 < len(s) + 1:
                way1 = True if s[i:i + 2] in options else False
                next1 = dp[i + 2] if i + 2 < len(s) else True
            if i + 3 < len(s) + 1:
                way2 = True if s[i:i + 3] in options else False
                next2 = dp[i + 3] if i + 3 < len(s) else True
            dp[i] = (way1 and next1) or (way2 and next2)
        print('YES' if dp[0] else 'NO')


if __name__ == '__main__':
    solution()
