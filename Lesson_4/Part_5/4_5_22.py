from zipfile import ZipFile
import json


def is_correct_json(data):
    try:
        ans = json.loads(data)
    except ValueError:
        return False
    else:
        return ans


with ZipFile("4_5_22_data.zip") as zip_data:
    footballers = []
    for i in zip_data.infolist():
        ans = i.filename
        if not i.is_dir() and ans[ans.find(".") + 1:] == "json":
            with zip_data.open(i.filename) as f:
                data_json = is_correct_json(f.read())
                if data_json and data_json["team"] == "Arsenal":
                    footballers.append(data_json["first_name"] + " " + data_json["last_name"])
    print(*sorted(footballers), sep="\n")