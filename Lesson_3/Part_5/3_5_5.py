from datetime import datetime

n = int(input())
people = {}
for i in range(n):
    i = input()
    birthday = datetime.strptime(i[-10:], '%d.%m.%Y')
    if birthday not in people.keys():
        people[birthday] = [i[:-10]]
    else:
        people[birthday].append([i[:-10]])

oldest = min(people.keys())
man = len(people[oldest]) if len(people[oldest]) > 1 else people[oldest][0]
print(datetime.strftime(oldest, '%d.%m.%Y'), man)
