def is_greater(lst, num):
    return any([sum(i) > num for i in lst])
