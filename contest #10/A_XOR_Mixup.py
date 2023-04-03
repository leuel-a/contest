#!/usr/bin/python3
"""Contest-10 Problem #A --> XOR Mixup"""


def main() -> None:
    test_cases = int(input())

    for _ in range(test_cases):
        n = int(input())
        arr = list(map(int, input().split()))

        for ind, elem in enumerate(arr):
            changed = 0
            for i in range(len(arr)):
                if i != ind:
                    changed ^= arr[i]

            if changed == arr[ind]:
                print(arr[ind])
                break



if __name__ == '__main__':
    main()
