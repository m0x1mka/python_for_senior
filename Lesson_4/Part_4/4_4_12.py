import json

with open("4_4_12_data.json", encoding="utf-8") as f:
    data = json.load(f)

with open("4_4_12_answer.csv", "w", encoding="utf-8") as fw:
    fw.write("name,phone\n")
    people = []
    for i in data:
        if i["age"] >= 18 and i["progress"] >= 75:
            people.append(i["name"] + "," + i["phone"] + "\n")
    for i in sorted(people):
        fw.write(i)
