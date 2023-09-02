from collections import Counter
import csv

with open("6_8_18_data.csv", encoding="utf-8") as f:
    data = [i[1] for i in list(csv.reader(f))[1:]]
    counted = Counter(data)
    for i in sorted(counted.keys()):
        print(f"{i}: {counted[i]}")