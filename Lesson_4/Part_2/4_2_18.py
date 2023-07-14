import csv

with open("4_2_18.csv", encoding="utf-8") as f:
    lst = list(csv.reader(f, delimiter=";"))
    new_lst = [i for i in lst if i[0] == "1" and float(i[-1]) < 18]
    men = []
    women = []
    for i in new_lst:
        if i[-2] == "male":
            men.append(i)
        else:
            women.append(i)
    lst = men + women
    for i in lst:
        print(i[1])
