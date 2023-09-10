#!/usr/bin/python3
"""Contest-10 Problem #E --> Powers of Two"""


def main() -> None:
    n, k = map(int, input().split())

    count_dict = {}
    for i in range(n.bit_length()):
        if n & (1 << i) == 0:
            count_dict = count_dict.get(i, 0) + 1
            


if __name__ == '__main__':
    main()
