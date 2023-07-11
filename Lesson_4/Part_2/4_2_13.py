with open("4_2_13.csv", encoding="utf-8") as f:
    salaries = [i.split(";") for i in f.readlines()]
    comps = {}
    for i in sorted(sorted(salaries[1:]), key=lambda x: int(x[1])):
        if i[0] not in comps.keys():
            comps[i[0]] = [int(i[1])]
        else:
            comps[i[0]].append(int(i[1]))
    for i in sorted(list(comps.keys()), key=lambda x: sum(comps[x])/len(comps[x])):
        print(i)