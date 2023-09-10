#!/usr/bin/python3
""""""


def mochaAndMath() -> None:
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))

        min_val = min(nums)
        for num in nums:
            min_val &= num
        print(min_val)


if __name__ == '__main__':
    mochaAndMath()
