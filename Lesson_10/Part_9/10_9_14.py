def first_true(itr, func):
    for i in itr:
        if func(i) if func is not None else i:
            return i
    return None
