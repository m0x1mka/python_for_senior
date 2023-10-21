def flatten(lst):
    for i in lst:
        if type(i) == int:
            yield i
        else:
            yield from flatten(i)
