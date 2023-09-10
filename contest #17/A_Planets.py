#!/usr/bin/python3
""""""
from collections import defaultdict
from heapq import heapify, heappop


def planets() -> None:
    t = int(input())

    for _ in range(t):
        n, c = map(int, input().split())
        a = list(map(int, input().split()))

        orbits = defaultdict(int)
        for idx, val in enumerate(a):
            orbits[val] += 1

        lst = [(val, key) for key, val in orbits.items()]
        heapify(lst)

        min_cost = 0
        while lst:
            num_of_planets, planet = heappop(lst)
            min_cost += min(num_of_planets, c)
        print(min_cost)

if __name__ == '__main__':
    planets()
