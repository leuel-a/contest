#!/usr/bin/python3
""""""
from collections import defaultdict


def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    graph = defaultdict(list)
    for i in range(1, n):
        x, y = map(int, input().split())
        graph[x].append(y)

    def dfs(node: int, cat: int) -> None:
        nonlocal m, count
        if cat > m:
            return

        if len(graph[node]) == 0:
            count += 1

        for val in graph[node]:
            if a[val - 1] == 1:
                dfs(val, cat + 1)
            else:
                dfs(val, 0)
    count = 0
    if a[0] == 1:
        dfs(0, 1)
    else:
        dfs(0, 0)
    print(count)

if __name__ == '__main__':
    main()
