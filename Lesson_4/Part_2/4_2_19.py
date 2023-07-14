from datetime import datetime
import csv

with open("4_2_19.csv", encoding="utf-8") as f:
    lst = list(csv.reader(f))
    dct = {}
    for i in lst[1:]:
        if i[1] not in dct.keys():
            dct[i[1]] = [[i[0], datetime.strptime(i[2], "%d/%m/%Y %H:%M")]]
        else:
            dct[i[1]].append([i[0], datetime.strptime(i[2], "%d/%m/%Y %H:%M")])
    with open("4_2_19_answer.csv", "w", encoding="utf-8") as fw:
        total = []
        for i in list(dct.items()):
            final_lst = [i[0]]
            max_time = max(i[1], key=lambda x: x[1])
            final_lst.append(max_time)
            total.append(final_lst)
        fw.write("username,email,dtime\n")
        for i in sorted(total, key=lambda x: x[0]):
            fw.write(f"{i[1][0]},{i[0]},{datetime.strftime(i[1][1], '%d/%m/%Y %H:%M')}\n")

