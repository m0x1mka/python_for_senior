def with_previous(itr):
    pr = None
    for i in itr:
        yield (i, pr)
        pr = i
