import csv

with open("4_2_17.csv", encoding="utf-8") as f:
    nets = list(csv.reader(f, delimiter=";"))
    nets_areas = {}
    for i in nets[1:]:
        if i[1] not in nets_areas.keys():
            nets_areas[i[1]] = int(i[-1])
        else:
            nets_areas[i[1]] += int(i[-1])
    lst = list(nets_areas.items())
    lst.sort(key=lambda x: x[0])
    for i in sorted(lst, key=lambda x: x[1], reverse=True):
        print(f"{i[0]}: {i[1]}")
