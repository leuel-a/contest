#!/usr/bin/python3
"""Problem A --> Fast Food Restaurant

Status:
"""


def solution():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())

        arr = ['d'] * a + ['c'] * b + ['p'] * c
        print(arr)


if __name__ == '__main__':
    solution()
