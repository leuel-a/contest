#!/usr/bin/python3
""""""
from heapq import heapify, heappop, heappush

def correctSolution() -> None:
    nums = list(map(int, input()))
    solution = int(input())
    if len(str(int(solution))) != len(nums):
        print('WRONG_ANSWER')
        exit()

    first = 0
    nums.sort()
    if nums[first] == 0:
        for i in range(len(nums)):
            if nums[i] != 0:
                break
        nums[first], nums[i] = nums[i], nums[first]
    min_val = int(''.join(str(val) for val in nums))
    print('OK' if min_val == solution else 'WRONG_ANSWER')

if __name__ == '__main__':
    correctSolution()
