import csv

with open("4_2_21.csv", encoding="utf-8") as f:
    letters = "АБВГ"
    ans = list(csv.reader(f))
    classes = {}
    start = ans[0]
    for i in range(len(ans[0])):
        for j in range(len(ans)):
            if start[i] not in classes.keys():
                classes[start[i]] = [ans[j][i]]
            else:
                classes[start[i]].append(ans[j][i])
    with open("4_2_21_answer.csv", "w", encoding="utf-8", newline="") as fw:
        writer = csv.writer(fw)
        s_list = sorted(list(classes.values())[1:], key=lambda x: letters.index(x[0][x[0].find("-") + 1:]))
        s_list = sorted(s_list, key=lambda x: int(x[0][:x[0].find("-")]))
        final = [list(classes.values())[0]] + s_list
        for i in range(len(final[0])):
            lst = [j[i] for j in final]
            writer.writerow(lst)
