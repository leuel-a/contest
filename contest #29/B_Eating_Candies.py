#!/usr/bin/python3
"""Contest Problem #B ==> Eating Candies"""


def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())
        w = list(map(int, input().split()))

        left_sum = [w[0]]
        for i in range(1, n):
            left_sum.append(left_sum[-1] + w[i])

        right_sum = w[:]
        prev = 0
        for i in range(n - 2, -1, -1):
            right_sum[i] += right_sum[i + 1]

        max_ = 0
        left, right = 0, n - 1
        while left < right:
            if left_sum[left] == right_sum[right]:
                max_ = n - right + left + 1
                left += 1
                right -= 1
            elif left_sum[left] > right_sum[right]:
                right -= 1
            else:
                left += 1
        print(max_)

if __name__ == '__main__':
    solution()
