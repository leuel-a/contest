#!/usr/bin/python3
""""""
from collections import defaultdict, deque, Counter


def foreverWinter() -> None:
    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        graph = defaultdict(list)
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        # length, index
        min_len = [-1, float('inf')]
        for key, val in graph.items():
            if len(val) > 1 and len(val) < min_len[1]:
                min_len[0], min_len[1] = len(val), key

        queue = deque([(min_len[1], 0)])
        color = [-1 for _ in range(n)]

        color[min_len[1] - 1] = 0
        while queue:
            node, c = queue.popleft()

            for neighbour in graph[node]:
                if color[neighbour - 1] == -1:
                    color[neighbour - 1] = 1 - c
                    queue.append((neighbour, 1 - c))

        dict_s = Counter(color)
        ones = min(dict_s[1], dict_s[0])
        zeros = max(dict_s[1], dict_s[0]) - 1
        print(ones, zeros // ones)

if __name__ == '__main__':
    foreverWinter()
