"""Contest #10D -> Rock And Lever"""
from typing import List
from math import comb
from collections import defaultdict


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        dict_s = defaultdict(int)
        for num in nums:
            msb = len(bin(num)[2:])
            dict_s[msb] += 1

        count = 0
        for value in dict_s.values():
            if value < 2:
                continue

            count += comb(value, 2)
        print(count)


solve()

