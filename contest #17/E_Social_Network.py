#!/usr/bin/python3
from typing import List
from collections import defaultdict

class DisJointSet:
    def __init__(self, n: int) -> None:
        self.rep = {i: i for i in range(1, n + 1)}
        self.size = defaultdict(lambda : 1)
        self.max = -1

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

        self.max = max(self.size[greater], self.max)


    def connected(self, x: tuple, y: tuple) -> bool:
        return self.representative(x) == self.representative(y)

def socialNetwork() -> None:
    n, d = map(int, input().split())

    uF = DisJointSet(n)
    for _ in range(d):
        a, b = map(int, input().split())
        uF.union(a, b)
        print(uF.max - 1)


if __name__ == '__main__':
    socialNetwork()
