#!/usr/bin/python3
""""""
from heapq import heapify, heappop, heappush


def koxiaAndWhiteboards() -> None:
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        heapify(a)
        i = 0
        while i < m:
            heappop(a)
            heappush(a, b[i])
            i += 1
        print(sum(a))


if __name__ == '__main__':
    koxiaAndWhiteboards()
