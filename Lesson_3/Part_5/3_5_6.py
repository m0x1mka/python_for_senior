from datetime import datetime

n = int(input())
people = {}
for i in range(n):
    i = input()
    birthday = datetime.strptime(i[-10:], '%d.%m.%Y')
    if birthday not in people.keys():
        people[birthday] = [i[:-10]]
    else:
        people[birthday].append(i[:-10])

max_len = len(max(list(people.values()), key=len))
for i in sorted(people.keys()):
    if len(people[i]) == max_len:
        print(datetime.strftime(i, '%d.%m.%Y'))
