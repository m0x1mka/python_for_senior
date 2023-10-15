from datetime import date, timedelta


def dates(start, count=None):
    if count is None:
        while True:
            yield start
            if start == date.max:
                break
            start += timedelta(days=1)
    else:
        new_count = 0
        while new_count != count:
            yield start
            if start == date.max:
                break
            start += timedelta(days=1)
            new_count += 1
