from datetime import date
import calendar


def get_days_in_month(year, month):
    d = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11,
         'Dec': 12}
    num_month = d[month[:3]]
    days = calendar.monthrange(year, num_month)[1]
    lst = []
    for i in range(1, days + 1):
        lst.append(date(year, num_month, i))
    return lst
