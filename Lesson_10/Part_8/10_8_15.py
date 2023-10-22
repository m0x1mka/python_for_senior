from itertools import count


def tabulate(func):
    for i in count(1):
        yield func(i)
