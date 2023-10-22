import itertools as it


def roundrobin(*args):
    for i in it.zip_longest(*args, fillvalue="12345"):
        yield from [j for j in i if j != "12345"]
