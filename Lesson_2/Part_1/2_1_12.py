def index_of_nearest(nums, num):
    nums = [abs(i - num) for i in nums]
    return -1 if not nums else nums.index(min(nums))


print(index_of_nearest([9, 5, 3, 2, 11], 4))
