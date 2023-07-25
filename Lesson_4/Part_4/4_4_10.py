import json

with open("4_4_10.json", encoding="utf-8") as f:
    data = json.load(f)

religions = {}
for i in data:
    if i["religion"] not in religions.keys():
        religions[i["religion"]] = [i["country"]]
    else:
        religions[i["religion"]].append(i["country"])

for key in religions.keys():
    lst = religions.get(key)
    religions[key] = sorted(lst)

with open("4_4_10_answer.json", "w", encoding="utf-8") as fw:
    json.dump(religions, fw)
