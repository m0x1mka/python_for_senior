def around(itr):
    itr = list(itr)
    pr = None
    for i in range(len(itr)):
        if i == len(itr) - 1:
            yield (pr, itr[i], None)
        else:
            yield (pr, itr[i], itr[i + 1])
        pr = itr[i]
