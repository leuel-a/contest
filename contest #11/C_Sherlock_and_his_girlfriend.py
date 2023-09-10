#!/usr/bin/python3
from collections import Counter


def main() -> None:
    n = int(input())
    is_prime = [True for i in range(1000000)]
    is_prime[0] = is_prime[1] = False


    d = 2
    colors = [1 for i in range(n)]
    while d * d <= 1000 and d <= n + 1:
        j = d * d
        while j <= 100000:
            is_prime[j] = False
            j += d
        d += 1
    print(colors)



if __name__ == '__main__':
    main()
