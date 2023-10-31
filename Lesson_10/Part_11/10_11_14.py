from itertools import groupby


def group_anagrams(data):
    for i, j in groupby(sorted(data, key=lambda x: "".join(sorted(list(x)))), key=lambda x: "".join(sorted(list(x)))):
        yield tuple(j)
