def pairwise(itr):
    itr = list(itr)
    for i in range(len(itr)):
        if i == len(itr) - 1:
            yield (itr[i], None)
        else:
            yield (itr[i], itr[i + 1])
