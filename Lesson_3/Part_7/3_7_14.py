from datetime import datetime, timedelta

year = int(input())
month = 1
current_date = datetime(year=year, month=month, day=1)
lst = []
while month < 13:
    current_date = datetime(year=year, month=month, day=1)
    counter = 0
    while counter != 3:
        if current_date.weekday() == 3:
            counter += 1
        current_date += timedelta(days=1)
    current_date -= timedelta(days=1)
    lst.append(current_date)
    counter = 0
    month += 1
for i in lst:
    print(datetime.strftime(i, '%d.%m.%Y'))
