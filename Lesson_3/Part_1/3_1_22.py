from datetime import date


def get_date_range(start, end):
    lst = list()
    lst.append(start)
    if start > end:
        start, end = sorted([start, end])
    while start < end:
        start = date.toordinal(start)
        start += 1
        start = date.fromordinal(start)
        lst.append(start)
    return lst


def saturdays_between_two_dates(start, end):
    lst = get_date_range(start, end)
    saturdays = 0
    for data in lst:
        if data.weekday() == 5:
            saturdays += 1
    return saturdays
