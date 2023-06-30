from datetime import date


def saturdays_between_two_dates(start, end):
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
    saturdays = 0
    for data in lst:
        if data.isoweekday() == 5:
            saturdays += 1
    return saturdays


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)

print(saturdays_between_two_dates(date1, date2))
