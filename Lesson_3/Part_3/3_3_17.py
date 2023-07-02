from datetime import datetime

with open("diary.txt", encoding="utf-8") as f:
    text = f.read()
    lst = text.split("\n\n")
    times = {i[:17]: i for i in lst}
    final_times = {}
    for i in times.keys():
        formed_time = datetime.strptime(i, "%d.%m.%Y; %H:%M")
        final_times[formed_time] = times[i]
    new_lst = []
    for i in sorted(list(final_times.keys())):
        new_lst.append(final_times[i])
    print(*new_lst, sep='\n\n')

