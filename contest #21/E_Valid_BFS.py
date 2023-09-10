#!/usr/bin/python3
""""""
from collections import deque
from typing import List, Optional


def validBFS():
    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    bfs = list(map(int, input().split()))
    visited = set()
    range_dict, curr = {}, 1

    queue = deque([0])
    visited.add(0)
    range_dict[0] = (0, 1)
    while queue:
        node = queue.popleft()
        curr_len = len(graph[node])

        for neighbour in graph[node]:
            if neighbour not in visited:
                range_dict[neighbour] = (curr, curr + curr_len)
                visited.add(neighbour)
                queue.append(neighbour)
        curr = curr + curr_len

    valid = True
    for idx, num in enumerate(bfs):
        a, b = range_dict[num - 1]

        if a <= idx < b:
            continue
        valid = False

    print('Yes' if valid else 'No')


if __name__ == '__main__':
    validBFS()
