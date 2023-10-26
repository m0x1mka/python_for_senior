from itertools import pairwise


def is_rising(itr):
    for i in pairwise(itr):
        if i[0] >= i[1]:
            return False
    return True
