#!/usr/bin/python3
from typing import List
from functools import cache


def main():
    n = int(input())
    prices = list(map(int, input().split()))

    def findProfit(idx: int, bought: int):
        if idx >= len(prices):
            return 0

        if bought:
            return max(
                findProfit(idx + 1, False) + prices[idx],
                findProfit(idx + 1, bought)
            )
        return max(
            findProfit(idx + 1, True) - prices[idx],
            findProfit(idx + 1, bought)
        )

    
