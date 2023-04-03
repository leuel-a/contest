def main() -> None:
    l, r = map(int, input().split())

    _max = 0
    for i in range(l + 1, r + 1):
        val = i ^ (i - 1)
        if _max < val:
            _max = val
    print(_max)


if __name__ == '__main__':
    main()
