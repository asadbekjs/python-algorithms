# list
# nums = [1, 2, 3, 4, 5, 5, 4, 3, 2]
# print(set(nums))
# set - {1, 2, 3, 4, 5}

N = int(input())
nums = list(map(int, input().split()))
# print(nums)
# print(set(nums))
no_duplicate_nums = set(nums)
no_duplicate_num = sum(no_duplicate_nums) * 2 - sum(nums)
print(no_duplicate_num)