from datetime import datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y')
print(datetime.strftime(current_date, '%d.%m.%Y'))
for i in range(2, 11):
    current_date += timedelta(days=i)
    print(datetime.strftime(current_date, '%d.%m.%Y'))
