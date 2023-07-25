import json

with open("4_4_7_data.json", encoding="utf-8") as f:
    data = json.load(f)


new_data = []
for i in range(len(data)):
    if type(data[i]) == str:
        lst = list(data[i]) + ['!']
        new_data.append(''.join(lst))
    elif type(data[i]) == bool:
        new_data.append(True if data[i] is False else False)
    elif type(data[i]) == int:
        new_data.append(data[i] + 1)
    elif type(data[i]) == list:
        new_data.append(data[i] * 2)
    elif type(data[i]) == dict:
        dct = data[i]
        dct['newkey'] = None
        new_data.append(dct)


with open('4_4_7_answer.json', 'w', encoding='utf-8') as fw:

    json.dump(new_data, fw)

