"""Contest #10E --> Powers of Two"""
from typing import List
from collections import defaultdict, deque


def solve():
    n, k = map(int, input().split())

    ans = defaultdict(int)
    queue = deque()

    for i in range(31):
        ...