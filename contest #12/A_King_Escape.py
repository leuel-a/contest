#!/usr/bin/python3

def main() -> None:
    n = int(input())

    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    target = list(map(int, input().split()))

    if bob[0] > alice[0]:
        bob[0] = 'Up'
    else:
        bob[0] = 'Down'

    if bob[1] < alice[1]:
        bob[1] = 'Right'
    else:
        bob[1] = 'Left'

    if target[0] > alice[0]:
        target[0] = 'Up'
    else:
        target[0] = 'Down'

    if target[1] < alice[1]:
        target[1] = 'Right'
    else:
        target[1] = 'Left'

    if target[0] == bob[0] and target[1] == bob[1]:
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    main()
