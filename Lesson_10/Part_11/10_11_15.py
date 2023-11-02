from itertools import groupby


def ranges(nums):
    data = groupby(nums, key=lambda x: nums.index(x) - x)
    lst = []
    for i, j in data:
        j = tuple(j)
        lst.append((j[0], j[-1]) if len(j) > 1 else j * 2)
    return lst
