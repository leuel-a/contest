#!/usr/bin/python3
""""""
from collections import deque


def computerGame() -> None:
    t = int(input())

    for _ in range(t):
        n = int(input())

        matrix = []
        matrix.append(list(map(int, input())))
        matrix.append(list(map(int, input())))

        def inbound(row: int, col: int) -> bool:
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

        queue = deque()

        queue.append((0, 0))
        matrix[0][0] = 1

        path_found = False
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        while queue:
            row, col = queue.popleft()

            for row_inc, col_inc in directions:
                new_row, new_col = row + row_inc, col + col_inc

                if inbound(new_row, new_col) and matrix[new_row][new_col] == 0:
                    if new_row == 1 and new_col == len(matrix[0]) - 1:
                        path_found = True
                    matrix[new_row][new_col] = 1
                    queue.append((new_row, new_col))

        if path_found:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    computerGame()
