def first_largest(itr, n):
    for i in enumerate(itr):
        if i[1] > n:
            return i[0]
    else:
        return -1
