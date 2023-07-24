import json
import sys

data = sys.stdin.read()
new_data = json.loads(data)
for i in new_data.items():
    first = i[0]
    last = i[1]
    print(first, end=": ")
    if type(last) == list:
        print(*last, sep=", ")
    else:
        print(last)
