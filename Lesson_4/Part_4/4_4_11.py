import csv
import json

with open("4_4_11_data.csv", encoding="utf-8") as f:
    data = list(csv.reader(f, delimiter=";"))[1:]

correct_data = {}
for i in data:
    region = i[1]
    district = i[2]
    address = i[3]
    if region not in correct_data.keys():
        correct_data[region] = {district: [address]}
    else:
        if district not in correct_data[region]:
            correct_data[region][district] = [address]
        else:
            correct_data[region][district].append(address)

with open("4_4_11_answer.json", "w", encoding="utf-8") as fw:
    json.dump(correct_data, fw)

