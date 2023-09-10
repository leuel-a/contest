#!/usr/bin/python3
"""Contest #22 --> Problem B: Coins

Status:

"""
from typing import List


def coins():
    ...


if __name__ == '__main__':
    coins()


results = {}

# Read the input and store the comparison results
for i in range(3):
    line = input().strip()
    coin1, symbol, coin2 = line
    if symbol == ">":
        results[(coin1, coin2)] = 1
        results[(coin2, coin1)] = -1
    else:
        results[(coin1, coin2)] = -1
        results[(coin2, coin1)] = 1

# Determine the relative weights of the coins
if (results.get(("A", "B"), 0) + results.get(("B", "C"), 0) + results.get(("A", "C"), 0)) == 0:
    print("Impossible")
else:
    if results.get(("A", "B"), 0) + results.get(("B", "C"), 0) + results.get(("A", "C"), 0) == 3:
        print("CBA")
    elif results.get(("A", "B"), 0) + results.get(("B", "C"), 0) + results.get(("A", "C"), 0) == -3:
        print("ABC")
    elif results.get(("A", "B"), 0) + results.get(("B", "C"), 0) + results.get(("A", "C"), 0) == 1:
        if results.get(("A", "B"), 0) == 1:
            print("ACB")
        elif results.get(("B", "C"), 0) == 1:
            print("CAB")
        else:
            print("ABC")
    else:
        if results.get(("A", "B"), 0) == -1:
            print("CAB")
        elif results.get(("B", "C"), 0) == -1:
            print("BCA")
        else:
            print("CBA")
