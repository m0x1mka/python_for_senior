from collections import Counter
import csv
from collections import defaultdict
import json

files = ["6_8_21_data1.csv", "6_8_21_data2.csv", "6_8_21_data3.csv", "6_8_21_data4.csv"]
total_data = defaultdict(int)
for i in files:
    with open(i, encoding="utf-8") as f:
        data = list(csv.reader(f))[1:]
        for j in data:
            total_data[j[0]] += sum([int(x) for x in j[1:]])

with open("6_8_21_data5.json", encoding="utf-8") as fr:
    data = json.load(fr)
    for i in data.items():
        total_data[i[0]] *= i[1]

print(sum(total_data.values()))
