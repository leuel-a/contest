#!/usr/bin/python3
""""""
from collections import Counter

def makeItDivisibleBy25() -> None:
    t = int(input())

    for _ in range(t):
        num = list(map(int, input()))
        numDict = Counter(num)

        count = 0
        while len(num) >= 2:
            last_two = int(''.join(str(i) for i in num[-2:]))
            if last_two % 25 == 0:
                break

            if num[-1] == 0 and (0 in numDict or 5 in numDict):
                num.pop(-2)
            elif num[-1] == 5 and (2 in numDict or 7 in numDict):
                num.pop(-2)
            else:
                num.pop()
            count += 1
        print(count)

if __name__ == '__main__':
    makeItDivisibleBy25()
