#!/usr/bin/python3
""""""
from collections import deque


def main():
    a, b, c, d = map(int, input().split())

    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(-1, -1), (1, 1), (1, -1), (-1, 1)],
        'K': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]
    }

    def inbound(row: int, col: int) -> bool:
        return 1 <= row <= 8 and 1 <= col <= 8

    queue = deque([(a, b, 'R', 0), (a, b, 'B', 0), (a, b, 'K', 0)])
    visited = set([(a, b, 'R'), (a, b, 'B'), (a, b, 'K')])

    result = {}
    while queue:
        row, col, type, moves = queue.popleft()
        if type in result:
            continue

        if row == c and col == d:
            result[type] = moves



        if type == 'R' or type == 'B':
            for direction in directions[type]:
                rInc, cInc = direction

                newRow = row + rInc
                newCol = col + cInc
                while inbound(newRow, newCol):
                    if (newRow, newCol, type) not in visited:
                        visited.add((newRow, newCol, type))
                        queue.append((newRow, newCol, type, moves + 1))
                    newRow += rInc
                    newCol += cInc
        else:
            for direction in directions[type]:
                rInc, cInc = direction

                newRow = row + rInc
                newCol = col + cInc
                if inbound(newRow, newCol) and (newRow, newCol, type) not in visited:
                    visited.add((newRow, newCol, type))
                    queue.append((newRow, newCol, type, moves + 1))

    print(result.get('R', 0), result.get('B', 0), result.get('K', 0))


main()
