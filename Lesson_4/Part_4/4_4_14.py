import json
import csv
from datetime import datetime

with open("4_4_14_data.csv", encoding="utf-8") as f:
    data = csv.DictReader(f)
    data.fieldnames[2] = "best_score"
    data = list(data)

new_data = []
for i in data:
    i["best_score"] = int(i["best_score"])
    new_data.append(i)

final_data = {}
for i in sorted(new_data, key=lambda x: x["email"]):
    if i["email"] not in final_data.keys():
        final_data[i["email"]] = i
    else:
        if i["best_score"] > final_data[i["email"]]["best_score"]:
            final_data[i["email"]] = i
        elif i["best_score"] == final_data[i["email"]]["best_score"]:
            if datetime.strptime(i["date_and_time"], "%Y-%m-%d %H:%M:%S") > datetime.strptime(
                    final_data[i["email"]]["date_and_time"], "%Y-%m-%d %H:%M:%S"):
                final_data[i["email"]] = i

lst_marks = list(final_data.values())
lst_marks.sort(key=lambda x: x["email"])

with open("4_4_14_answer.json", "w", encoding="utf-8") as fw:
    json.dump(lst_marks, fw)
