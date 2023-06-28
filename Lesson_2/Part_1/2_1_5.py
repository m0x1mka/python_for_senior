def same_parity(nums):
    return [i for i in nums if i % 2 == nums[0] % 2]


print(same_parity([3, 5, 4, 7, 6, 9, 1]))
