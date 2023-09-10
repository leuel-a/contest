#!/usr/bin/python3
""""""
from typing import List


def solution() -> None:
    n, k = map(int, input().split())
    heights = list(map( int, input().split()) )

    prefix_sum = [0, heights[0]]
    for i in range(1, len(heights)):
        prefix_sum.append(prefix_sum[-1] + heights[i])

    _min = (-1, float('inf'))
    i, j = 0, k
    while j < len(prefix_sum):
        _min_idx, _min_val = _min
        curr_sum = prefix_sum[j] - prefix_sum[i]
        if curr_sum < _min_val:
            _min_idx = i + 1
            _min_val = curr_sum
        _min = (_min_idx, _min_val)
        i += 1
        j += 1
    print(_min[0])


if __name__ == '__main__':
    solution()
