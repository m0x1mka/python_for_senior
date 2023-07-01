from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
    except ValueError:
        return False
    else:
        return True
