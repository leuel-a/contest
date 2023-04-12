#!/usr/bin/python3
"""Contest-11 Problem #A --> Love Triangle"""
from collections import Counter


def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))

    for i in range(1, n+1):
        if nums[nums[nums[i - 1] - 1] - 1] == i:
            print('YES')
            break
    else:
        print('NO')


if __name__ == '__main__':
    main()
