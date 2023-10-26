from itertools import tee, chain


def ncycles(itr, num):
    new_itr = tee(itr, num)
    for i in range(num):
        yield from new_itr[i]
