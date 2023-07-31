import json

with open("4_4_15_data.json", encoding="utf-8") as f:
    data = json.load(f)

districts = {}
names = {}
for i in data:
    if i["OperatingCompany"]:
        if i["OperatingCompany"] not in names.keys():
            names[i["OperatingCompany"]] = 1
        else:
            names[i["OperatingCompany"]] += 1

    if i["District"] not in districts.keys():
        districts[i["District"]] = 1
    else:
        districts[i["District"]] += 1

max_district = [0, 0]
max_names = [0, 0]
for i in districts.items():
    if i[1] > max_district[1]:
        max_district = i
for i in names.items():
    if i[1] > max_names[1]:
        max_names = i

print(*max_district, sep=": ")
print(*max_names, sep=": ")

