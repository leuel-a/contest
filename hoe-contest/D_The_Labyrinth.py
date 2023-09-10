#!/usr/bin/python3
""""""
from collections import deque


def main():
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(input()))

    visited = set()
    queue = deque()
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0)
    ]

    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m

    result_matrix = [row[:] for row in graph]

    def breadth_first_search(row, col) -> int:
        size = 0
        visited.clear()

        queue.append((row, col))
        visited.add((row, col))

        while queue:
            x, y = queue.popleft()

            for x_in, y_in in directions:
                new_row = x + x_in
                new_col = y + y_in

                if inbound(new_row, new_col) and (new_row, new_col) not in visited and graph[new_row][new_col] != '*':
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
                    size += 1
        return size

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '*':
                size = breadth_first_search(i, j)
                result_matrix[i][j] = size + 1
    for row in result_matrix:
        print(''.join(str(val) for val in row))

    print()
main()
