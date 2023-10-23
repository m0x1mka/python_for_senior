from itertools import dropwhile


def drop_while_negative(itr):
    return dropwhile(lambda x: x < 0, itr)
