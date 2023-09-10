#!/usr/bin/python3
""""""


def main() -> None:
    n, t = map(int, input().split())
    nums = list(map(int, input().split()))

    i = 0
    while i < t - 1:
        i += nums[i]

    if i == (t - 1):
        print('YES')
    else:
        print('NO')



if __name__ == '__main__':
    main()
