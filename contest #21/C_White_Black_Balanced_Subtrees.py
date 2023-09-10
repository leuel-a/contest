#!/usr/bin/python3
"""Status Solved During Exam """
import sys
from typing import List, Optional


def whiteBlackBalancedSubtrees():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        s = list(input())

        graph = [[] for _ in range(n)]

        for idx, val in enumerate(a):
            graph[val - 1].append(idx + 1)

        def depth_first_search(node: Optional[int]):
            nonlocal count

            blacks, whites = 0, 0
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    b, w = depth_first_search(neighbour)
                    blacks += b
                    whites += w

            if s[node] == 'B':
                blacks += 1
            else:
                whites += 1


            if blacks == whites:
                count += 1
            return (blacks, whites)

        count, visited = 0, set()
        sys.setrecursionlimit(10000)
        depth_first_search(0)
        print(count)


if __name__ == '__main__':
    whiteBlackBalancedSubtrees()
