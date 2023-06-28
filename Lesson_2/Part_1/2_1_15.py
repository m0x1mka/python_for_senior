def get_biggest(nums):
    if not nums:
        return -1
    str_nums = [str(i) for i in nums]
    max_len = len(max(str_nums, key=len))
    new_nums = sorted(str_nums, reverse=True, key=lambda x: str(x) * max_len)
    return int(''.join(new_nums))


print(get_biggest([61, 228, 9, 3, 11]))
