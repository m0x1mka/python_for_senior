from datetime import datetime, timedelta


def num_of_sundays(year):
    date = datetime(year=year, month=1, day=1)
    if date.weekday() != 0 and year % 4 == 0:
        return 53
    else:
        return 52
