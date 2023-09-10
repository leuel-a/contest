#!/usr/bin/python3
"""Contest Problem #A ==> I wanna be the guy"""


def solution():
    n = int(input())
    a = set(list(map(int, input().split()))[1:])
    b = set(list(map(int, input().split()))[1:])

    union = a.union(b)
    print('I become the guy.' if len(union) == n else 'Oh, my keyboard!')


if __name__ == '__main__':
    solution()
