nums = list(map(int, input().split()))
print(nums)

s = sum(nums)
mn = min(nums)
mx = max(nums)

min_sum = s - mx
max_sum = s - mn

print(min_sum, max_sum)