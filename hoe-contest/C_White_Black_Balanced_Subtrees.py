#!/usr/bin/python3
""""""
import sys, threading
input = sys.stdin.readline
from collections import defaultdict
input = sys.stdin.readline
from typing import Tuple


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        color = list(input())

        count = 0
        graph = defaultdict(list)
        visited = set()

        for i, val in enumerate(a):
            graph[i + 2].append(val)
            graph[val].append(i + 2)

        g = [[0, 0] for _ in range(n)]

        def depth_first_search(node):
            visited.add(node)

            if color[node - 1] == 'B':
                g[node - 1][0] += 1
            else:
                g[node - 1][1] += 1

            for neighbour in graph[node]:
                if neighbour not in visited:
                    depth_first_search(neighbour)
                    b, w = g[neighbour - 1]
                    g[node - 1][0] += b
                    g[node - 1][1] += w

        depth_first_search(1)

        count = 0
        for a, b in g:
            if a == b:
                count += 1
        print(count)


# Set the stack size
threading.stack_size(1 << 27)

# Create and start the main thread
main_thread = threading.Thread(target=main)
main_thread.start()

# Wait for the main thread to complete
main_thread.join()

