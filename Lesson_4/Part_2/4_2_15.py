import csv


def csv_columns(filename):
    with open(filename, encoding="utf-8") as f:
        cols = list(csv.reader(f))
        name_dict = {}
        for i in cols[0]:
            name_dict[i] = []
        for i in range(len(cols[0])):
            for j in cols[1:]:
                name_dict[cols[0][i]].append((j[i]))
    return name_dict


print(csv_columns("4_2_15.csv"))
