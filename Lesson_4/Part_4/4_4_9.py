import json

with open("4_4_9_data.json", encoding="utf-8") as f:
    data = json.load(f)

new_dict = {}
for i in data:
    new_dict.update(i)

for key in new_dict.keys():
    new_dict[key] = None

for i in range(len(data)):
    dct = data[i]
    new_dct = new_dict | dct
    data[i] = new_dct

with open("4_4_9_answer.json", "w", encoding="utf-8") as fw:
    json.dump(data, fw)
