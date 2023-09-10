#!/usr/bin/python3
"""Contest-10 Problem #F --> Little Girl and Maximum XOR"""


def main() -> None:
    l, r = map(int, input().split())

    for i in range(r.bit_length() - 1):
        if r & (1 << i) != 0:
            r &= ~(1 << i)
        l |= 1 << i
    print(r ^ l)

if __name__ == '__main__':
    main()
