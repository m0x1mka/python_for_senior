from datetime import datetime

dif = []
lst = input().split()
lst = [datetime.strptime(i, '%d.%m.%Y') for i in lst]
for i in range(len(lst) - 1):
    dif.append(abs(lst[i] - lst[i + 1]))
print([i.days for i in dif])
