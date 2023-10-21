def filterfalse(predicate, iterable):
    if predicate is not None:
        return [i for i in iterable if predicate(i) == False]
    return [i for i in iterable if not i]
