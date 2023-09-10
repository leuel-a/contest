#!/usr/bin/python3
""""""


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        print(sum(nums) - min(nums) * n)


main()
