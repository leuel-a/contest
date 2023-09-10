#!/usr/bin/python3
""""""

def minimumVariedNumber() -> None:
    t = int(input())

    for _ in range(t):
        num = int(input())

        stack, curr_sum = [], 0
        for i in range(9, 0, -1):
            if curr_sum + i > num:
                continue
            stack.append(i)
            curr_sum += i
        print(''.join(str(val) for val in stack[::-1]))

if __name__ == '__main__':
    minimumVariedNumber()
