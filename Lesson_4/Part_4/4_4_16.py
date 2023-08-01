import json

with open("4_4_16_data.json", encoding="utf-8") as f:
    data = json.load(f)

kinds = {}
for i in data:
    if i["TypeObject"] not in kinds.keys():
        kinds[i["TypeObject"]] = [i["Name"], i["SeatsCount"]]
    elif i["TypeObject"] in kinds.keys() and i["SeatsCount"] > kinds[i["TypeObject"]][1]:
        kinds[i["TypeObject"]] = [i["Name"], i["SeatsCount"]]

for i in sorted(kinds.items(), key=lambda x: x[0]):
    print(f"{i[0]}: {i[1][0]}, {i[1][1]}")
