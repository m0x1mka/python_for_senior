def grouper(itr, n):
    lst = list(itr)
    groups = []
    for i in range(len(lst) // n + 1):
        new = []
        for i in range(n):
            if len(lst) >= 1:
                el = lst[0]
                new.append(el)
                del lst[0]
            else:
                new.append(None)
        if set(new) != set([None]):
            groups.append(tuple(new))
    return groups
