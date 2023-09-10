#!/usr/bin/python3
""""""
from typing import List


def solution() -> None:
    t = int(input())

    for _ in range(t):
        n, lunch_time = map(int, input().split())

        durations = list(map(int, input().split()))
        entertainment = list(map(int, input().split()))

        _max = -1
        idx, time = 0, 0
        while idx < n:
            if time + durations[idx] <= lunch_time:
                if _max == -1 or entertainment[_max] < entertainment[idx]:
                    _max = idx
            time += 1
            idx += 1
        print(_max + 1 if _max != -1 else _max)


if __name__ == '__main__':
    solution()
