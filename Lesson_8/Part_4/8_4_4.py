def recursive_sum(nums):
    counter = 0
    if len(nums) == 0:
        return 0
    else:
        for i in nums:
            if type(i) == int:
                counter += i
            else:
                counter += recursive_sum(i)
    return counter
