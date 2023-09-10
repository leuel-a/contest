#!/usr/bin/python3
from typing import List
from collections import defaultdict

class DisJointSet:
    def __init__(self, n: int) -> None:
        self.rep = {i: i for i in range(1, n + 1)}
        self.size = defaultdict(lambda : 1)

    def representative(self, node: tuple) -> int:
        parent = node
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != parent:
            prev = self.rep[node]
            self.rep[node] = parent
            node = prev
        return parent

    def union(self, x: tuple, y: tuple) -> None:
        xrep = self.representative(x)
        yrep = self.representative(y)

        if xrep == yrep:
            return

        greater = xrep if self.size[xrep] >= self.size[yrep] else yrep
        smaller = xrep if greater == yrep else yrep

        self.rep[smaller] = greater
        self.size[greater] += self.size[smaller]


    def connected(self, x: tuple, y: tuple) -> bool:
        return self.representative(x) == self.representative(y)

def newsDistribution() -> None:
    n, m = map(int, input().split())

    uF = DisJointSet(n)
    for i in range(1, m + 1):
        k = list(map(int, input().split()))
        lst = k[1:]

        for i in range(1, len(lst)):
            uF.union(lst[i], lst[i - 1])

    res = []
    for i in range(1, n + 1):
        res.append(uF.size[uF.representative(i)])
    print(' '.join(str(val) for val in res))

if __name__ == '__main__':
    newsDistribution()
