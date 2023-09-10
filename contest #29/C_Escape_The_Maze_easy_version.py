#!/usr/bin/python3
"""Contest Problem #C --> Escape The Maze (easy version)"""
from collections import deque


def solution():
    t = int(input())

    for _ in range(t):
        input()
        n, k = map(int, input().split())
        friends = list(map(int, input().split()))

        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            a, b = map(int, input().split())
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)

        queue = deque()
        print(friends)



if __name__ == '__main__':
    solution()
