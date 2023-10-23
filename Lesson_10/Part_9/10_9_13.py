from itertools import dropwhile


def drop_this(itr, obj):
    return dropwhile(lambda x: x == obj, itr)
