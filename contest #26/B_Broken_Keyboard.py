#!/usr/bin/python3


def solution():
    t = int(input())

    for _ in range(t):
        s = input()

        res, i = set(), 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i + 1]:
                i += 2
            else:
                res.add(s[i])
                i += 1
        print(''.join(str(char) for char in sorted(res)))


if __name__ == '__main__':
    solution()
