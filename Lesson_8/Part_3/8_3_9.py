def range_sum(lst, start, stop):
    if start == stop:
        return lst[start]
    return lst[stop] + range_sum(lst, start, stop - 1)
