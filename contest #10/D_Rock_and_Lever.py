def main() -> None:
    tests = int(input())

    for _ in range(tests):
        n = int(input())
        nums = list(map(int, input().split()))

        def merge_sort(nums: list[int]) -> int:
            count = 0

            def divide(start: int, end: int) -> list[int]:
                if start == end:
                    return [nums[start]]

                mid = start + (end - start) // 2
                left_side = divide(start, mid)
                right_side = divide(mid + 1, end)
                return merge(left_side, right_side)

            def merge(left_side: list[int], right_side: list[int]) -> list[int]:
                nonlocal count
                i, j = 0, 0

                while j < len(right_side):
                    while i < len(left_side) and (left_side[i] & right_side[j] < left_side[i] ^ right_side[j]):
                        i += 1
                    count += len(left_side) - i
                    j += 1


                res, leftPtr, rightPtr = [], 0, 0
                while leftPtr < len(left_side) and rightPtr < len(right_side):
                    if left_side[leftPtr] <= right_side[rightPtr]:
                        res.append(left_side[leftPtr])
                        leftPtr += 1
                    else:
                        res.append(right_side[rightPtr])
                        rightPtr += 1

                res.extend(left_side[leftPtr:])
                res.extend(right_side[rightPtr:])
                return res

            divide(0, len(nums) - 1)
            return count

        count = merge_sort(nums)
        print(count)

if __name__ == '__main__':
    main()
