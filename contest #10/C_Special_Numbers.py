#!/usr/bin/python3
"""Contest-10 Problem #C --> Special Numbers"""


def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        n, k = map(int, input().split())
        special_number = 0
        for i in range(k.bit_length()):
            if k & (1 << i) != 0:
                special_number += n ** i
        print(special_number % (10 ** 9 + 7))

if __name__ == '__main__':
    main()
