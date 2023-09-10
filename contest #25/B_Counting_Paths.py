#!/usr/bin/python3
"""Contest Problem: B Counting Paths"""
from collections import defaultdict, deque
from typing import List, Optional, Tuple, Deque # noqa: F401


def solution():
    t = int(input())

    for _ in range(t):
        directions = ["Left", "Right"]
        max_path, max_change = map(int, input().split())

        count = 0
        queue = deque([("Left", 1, 0), ("Right", 1, 0)])
        visited = set([("Left", 1, 0), ("Right", 1, 0)])
        while queue:
            direction, path, change = queue.popleft()
            if path == max_path and change == max_change:
                count += 1
                continue
            for neighbour in directions:
                if neighbour != direction and (neighbour, path + 1, change + 1) not in visited:
                    visited.add((neighbour, path + 1, change + 1))
                    queue.append((neighbour, path + 1, change + 1))
        print(count)


if __name__ == "__main__":
    solution()

