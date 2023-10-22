import itertools as it
import string


def alnum_sequence():
    lst = []
    for i in range(26):
        lst.append(i + 1)
        lst.append(string.ascii_uppercase[i])
    return it.cycle(lst)
