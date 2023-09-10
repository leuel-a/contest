#!/usr/bin/python3
""""""
from collections import defaultdict


def reposts() -> None:
    n = int(input())
    graph = defaultdict(list)
    visited = set()

    for _ in range(n):
        line = input().split()
        graph[line[0].lower()].append(line[2].lower())
        graph[line[2].lower()].append(line[0].lower())

    def depth_first_search(name: int, depth: int):
        nonlocal max_depth

        visited.add(name)
        for repost in graph[name]:
            if repost not in visited:
                depth_first_search(repost, depth + 1)
        max_depth = max(max_depth, depth)


    max_depth = float('-inf')
    depth_first_search('polycarp', 1)
    print(max_depth)

if __name__ == '__main__':
    reposts()
