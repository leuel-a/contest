#!/usr/bin/python3
""""""
from collections import defaultdict, Counter
from typing import List
import sys, threading
input = sys.stdin.readline
input = sys.stdin.readline


def main():
    n, l, r = map(int, input().split())
    dp = {}
    dp[1] = [1]

    def find(n: int) -> List[int]:
        if n in dp:
            return dp[n]

        val = find(n // 2)
        result = [*val, n % 2, *val]
        dp[n] = result
        return dp[n]

    finalResult = find(n)
    ones = Counter(finalResult[l - 1:r])[1]
    print(ones)


sys.setrecursionlimit(1 << 30)

threading.stack_size(1 << 27)

main_thread = threading.Thread(target = main)

main_thread.start()

main_thread.join()


