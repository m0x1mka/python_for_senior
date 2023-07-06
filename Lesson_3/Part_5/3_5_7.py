from datetime import datetime, timedelta

current_date = datetime.strptime(input(), '%d.%m.%Y')
dates = []
for i in range(1, 8):
    dates.append(current_date + timedelta(days=i))

workers = {}
for i in range(int(input())):
    worker = input().split()
    birthday = datetime.strptime(worker[2], '%d.%m.%Y')
    for j in dates:
        if birthday.day == j.day and birthday.month == j.month:
            workers[birthday] = worker[0] + ' ' + worker[1]
print(workers[max(workers.keys())] if workers else "Дни рождения не планируются")
