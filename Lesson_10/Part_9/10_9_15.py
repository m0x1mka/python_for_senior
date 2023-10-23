from itertools import islice


def take(itr, n):
    return islice(itr, 0, n)
