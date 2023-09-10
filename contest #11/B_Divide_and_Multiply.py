#!/usr/bin/python3
""""""

def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        nums = list(map(int, input().split()))

        for i, elem in enumerate(nums):
            if elem % 2 == 0:
                


if __name__ == '__main__':
    main()
