import csv

with open("10_7_8_data.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))

total = 0
for i in data:
    if i[-1] == "a":
        total += int(i[1])

print(total)
