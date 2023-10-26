from itertools import pairwise


def max_pair(itr):
    max_sum = 0
    for i in pairwise(itr):
        if sum(i) > max_sum:
            max_sum = sum(i)
    return max_sum
