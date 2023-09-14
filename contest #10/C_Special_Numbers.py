"""Contest #10C --> Special Numbers"""
from typing import List


def solve():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        result = 0
        bit_str = list(map(int, str(bin(k)[2:])[::-1]))
        for i in range(len(bit_str)):
            result += (pow(n, i) * bit_str[i])
        
        print(result % (pow(10, 9) + 7))


solve()