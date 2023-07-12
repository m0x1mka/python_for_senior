import csv

col = int(input())
with open("4_2_14.csv", encoding="utf-8") as f:
    cols = list(csv.reader(f))
    cols.sort(key=lambda x: int(x[col - 1]) if x[col-1].isdigit() else x[col - 1])
    for i in cols:
        print(",".join(i))
