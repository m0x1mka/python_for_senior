from collections import ChainMap
import json

with open("6_9_22_data.json", encoding="utf-8") as f:
    data = json.load(f)

final_data = ChainMap(*data)
print(sum(final_data.values()))
