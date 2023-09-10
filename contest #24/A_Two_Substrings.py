#!/usr/bin/python3
"""Contest Problem --> A. Two Substrings

Status:
"""
from collections import Counter, defaultdict
from typing import List, Optional, Tuple


def solution():
    string = input()

    strCount = Counter(string)
    if strCount['A'] < 2 or strCount['B'] < 2:
        print('NO')
        return

    dict_s = defaultdict(int)
    i = 0
    while i < len(string):
        if string[i] == 'A' and (i + 1) < len(string) and string[i + 1] == 'B':
            dict_s['AB'] += 1
        elif string[i] == 'B' and (i + 1) < len(string) and string[i + 1] == 'A':
            dict_s['BA'] += 1
        i += 1
    print('YES' if len(dict_s) == 2 else 'NO')


if __name__ == '__main__':
    solution()
