#!/usr/bin/python3
""""""

def main() -> None:
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())

        for i in range(a, b + 1):
            if b % a == 0:
                print(a, b)
                break
if __name__ == '__main__':
    main()
