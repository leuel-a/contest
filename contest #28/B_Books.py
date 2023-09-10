n, t = map(int, input().split())
nums = list(map(int, input().split()))

prefix_sum = [0]
for i in range(len(nums)):
    prefix_sum.append(prefix_sum[-1] + nums[i])


max_ = -1
left = 0
for right in range(len(prefix_sum)):
    curr = prefix_sum[right] - prefix_sum[left]

    while curr > t and left < right:
        curr -= nums[left]
        left += 1
    max_ = max(max_, right - left)
print(max_)
