from datetime import date


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


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')
