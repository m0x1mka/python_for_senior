def get_date_range(start, end):
    lst = list()
    lst.append(start)
    if start > end:
        return []
    else:
        while start < end:
            start = date.toordinal(start)
            start += 1
            start = date.fromordinal(start)
            lst.append(start)
    return lst