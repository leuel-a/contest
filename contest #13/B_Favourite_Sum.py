#!/usr/bin/python3
""""""


def main() -> None:
    t = int(input())

    for _ in range(t):
        n, x = map(int, input().split())
        favorites = list(map(int, input().split()))

        _sum = (x * (x + 1)) // 2
        for num in favorites:
            if 1 <= num <= x:
                _sum -= (2 * num)
        print(_sum)

if __name__ == '__main__':
    main()
