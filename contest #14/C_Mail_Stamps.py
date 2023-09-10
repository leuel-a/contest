#!/usr/bin/python3
""""""
(from collections import defaultdict, deque
import sys

sys.setrecursionlimit(4000)


def mailStamps():
    graph = defaultdict(list)
    num_of_stamps = int(input())

    for _ in range(num_of_stamps):
        a, b = input().split()
        graph[a].append(b)
        graph[b].append(a)

    for k in graph.keys():
        if len(graph[k]) == 1:
            start = k
            break

    queue = deque([start])
    visited = set([start])

    path = []
    while queue:
        val = queue.popleft()
        path.append(val)

        for neighbour in graph[val]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print(' '.join(str(val) for val in path))


if __name__ == '__main__':
    mailStamps())
