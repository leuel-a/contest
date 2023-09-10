#!/usr/bin/python3
"""Contest Problem B --> Deadline"""
from typing import List, Tuple, DefaultDict, Deque
from math import ceil


def solution():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split())
        if d <= n:
            print('YES')
        else:
            for i in range(1, n + 1):
                if ceil(d / (i + 1)) + i <= n:
                    print('YES')
                    break
            else:
                print('NO')

if __name__ == '__main__':
    solution()
