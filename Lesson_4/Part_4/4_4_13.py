import json

with open("4_4_13_data.json", encoding="utf-8") as f:
    data = json.load(f)

pools = []
for i in data:
    times = i["WorkingHoursSummer"]["Понедельник"].split("-")
    start = int(times[0].split(":")[0])
    end = int(times[1].split(":")[0])
    if start <= 10 and end >= 12:
        pools.append(i)

max_length = 0
for i in pools:
    if i["DimensionsSummer"]["Length"] > max_length:
        max_length = i["DimensionsSummer"]["Length"]

length_pools = []
for i in pools:
    if i["DimensionsSummer"]["Length"] == max_length:
        length_pools.append(i)

max_width = length_pools[1]["DimensionsSummer"]["Width"]
print(f"{max_length}x{max_width}")
print(length_pools[1]["Address"])
