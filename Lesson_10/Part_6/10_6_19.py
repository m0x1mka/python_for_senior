def interleave(*args):
    lst = zip(*args)
    return [i for j in lst for i in j]
