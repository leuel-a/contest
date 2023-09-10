#!/usr/bin/python3
""""""
from typing import List, Optional
from heapq import heapify, heappop, heappush


def benches():
    n = int(input())
    m = int(input())

    a = []
    for _ in range(n):
        a.append(int(input()))

    _max = max(a) + m
    
    heapify(a)
    for _ in range(m):
        val = heappop(a)
        heappush(a, val + 1)
    print(max(a), _max)

if __name__ == '__main__':
    benches()
