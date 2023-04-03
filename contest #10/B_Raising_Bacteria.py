def main() -> None:
    x = int(input())

    bacterias = 0
    while x > 0:
        if x % 2 != 0:
            bacterias += 1
        x //= 2
    print(bacterias)
if __name__ == '__main__':
    main()
