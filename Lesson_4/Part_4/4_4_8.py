import json

with open("4_4_8_data1.json", encoding="utf-8") as f:
    data1 = json.load(f)

with open("4_4_8_data2.json", encoding="utf-8") as f:
    data2 = json.load(f)

data1.update(data2)
with open("4_4_8_answer.json", "w", encoding="utf-8") as f:
    json.dump(data1, f)