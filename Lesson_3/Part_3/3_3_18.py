from datetime import datetime, date


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


def format_dates(start, end):
    start = datetime.strptime(start, "%d.%m.%Y")
    end = datetime.strptime(end, "%d.%m.%Y")
    start = date(start.year, start.month, start.day)
    end = date(end.year, end.month, end.day)
    return get_date_range(start, end)


def is_available_date(dates, some_date):
    for i in range(len(dates)):
        if len(dates[i]) != 10:
            start, end = dates[i].split('-')
            dates[i] = [date.strftime(i, "%d.%m.%Y") for i in format_dates(start, end)]
    if '-' not in some_date:
        for i in dates:
            if i == some_date or some_date in i:
                return False
        return True
    else:
        start, end = some_date.split('-')
        dates_to_book = [date.strftime(i, "%d.%m.%Y") for i in format_dates(start, end)]
        for i in dates_to_book:
            for j in dates:
                if i == j or i in j:
                    return False
        return True
