t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    # Loop over the array and check if I have the parity
    # 14 -> Even
    # Search -> Even
    left, right = 0, 1
    while right < len(nums):
        curr = nums[left]

        if (curr + nums[right]) % 2 != 0 or left == right:
            right +=1
        else:
            nums[left + 1], nums[right] = nums[right], nums[left + 1]
            left += 1
        # Brute Force Way
        # for i in range(left + 1, len(nums)):
        #     if (nums[i] + nums[left]) % 2 == 0:
        #         nums[i], nums[left + 1] = nums[left + 1], nums[i]
        # left += 1

    print(*nums)

