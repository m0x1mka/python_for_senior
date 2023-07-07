from datetime import date, timedelta


def get_all_mondays(year):
    mondays = []
    next_year = year + 1
    start = date(year, 1, 1)
    while start.weekday() != 0:
        start += timedelta(days=1)
    mondays.append(start)
    while start.year < next_year:
        start += timedelta(days=7)
        mondays.append(start)
    return mondays[:-1]


print(get_all_mondays(111))
