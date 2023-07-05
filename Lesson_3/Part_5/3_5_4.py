from datetime import datetime, timedelta

a = datetime.strptime(input(), '%d.%m.%Y')
b = datetime.strptime(input(), '%d.%m.%Y')

start = False
add=1
while a <= b:
    if (a.day+a.month)%2 == 1:
        start = True
        add = 3
    if start:
        if a.weekday() not in [0, 3]:
            print(datetime.strftime(a, '%d.%m.%Y'))
    a += timedelta(days=add)
