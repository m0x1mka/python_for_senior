from datetime import datetime, date, timedelta


def fill_up_missing_dates(dates):
    lst = [datetime.strptime(i, '%d.%m.%Y') for i in dates]
    current_date = min(lst)
    final_lst = [min(lst)]
    while current_date < max(lst):
        current_date += timedelta(days=1)
        final_lst.append(current_date)
    return [datetime.strftime(i, '%d.%m.%Y') for i in final_lst]
