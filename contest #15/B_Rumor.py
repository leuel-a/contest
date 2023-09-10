#!/usr/bin/python3
""""""
from collections import defaultdict, deque


def rumor() -> None:
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))

    graph = defaultdict(list)
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)

    def depth_first_search(node: int, min_cost: int) -> int:
        stack = [node]

        while stack:
            val = stack.pop()
            visited.add(val)

            for neighbour in graph[val]:
                if neighbour not in visited:
                    min_cost = min(min_cost, gold[neighbour - 1])
                    stack.append(neighbour)
        return min_cost

    visited, cost = set(), 0
    for i in range(1, n + 1):
        if i not in visited:
            cost += depth_first_search(i, gold[i - 1])
    print(cost)
if __name__ == '__main__':
    rumor()
