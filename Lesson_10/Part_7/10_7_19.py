from collections import Counter


def unique(itr):
    obj = Counter(itr)
    for i in obj:
        yield i
