from datetime import datetime, timedelta


def years_days(year):
    current_date = datetime(year, 1, 1)
    for i in range(366 if year % 400 == 0 else 365):
        yield datetime.strftime(current_date, "%Y-%m-%d")
        current_date += timedelta(days=1)
