"""Contest #10 Problem B --> Raising Bacteria"""
from typing import List


def solve():
    n = int(input())

    count = 0
    bit_mask = 1
    for i in range(n.bit_length()):
        if n & (bit_mask << i) != 0:
            count += 1

    print(count)
solve()