import csv
from datetime import datetime

with open("6_4_12_data.csv", encoding="utf-8") as f:
    data = list(csv.reader(f))
    for i in sorted(data[1:], key=lambda x: datetime.strptime(x[2] + " " + x[3], "%d.%m.%Y %H:%M")):
        print(i[0] + " " + i[1])
