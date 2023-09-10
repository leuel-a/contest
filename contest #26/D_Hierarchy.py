#!/usr/bin/python3
"""Contest Problem D --> Heirarchy"""
from collections import deque


def solution():
    n = int(input())
    q = list(map(int, input().split()))
    m = int(input())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a - 1].append((b - 1, c))

    qP = [(val, idx) for idx, val in enumerate(q)]
    qP.sort(reverse=True)

    visited = set()
    queue = deque()
    min_cost = 0

    for _, idx in qP:
        if idx not in visited and len(graph[idx]) > 0:
            visited.add(idx)
            queue.append(idx)

            while queue:
                node = queue.popleft()

                for j, cost in graph[node]:
                    if j not in visited:
                        visited.add(j)
                        queue.append(j)
                        min_cost += cost
    print(min_cost if len(visited) == n else -1)


if __name__ == '__main__':
    solution()
