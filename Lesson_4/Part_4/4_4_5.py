import json


def is_correct_json(data):
    try:
        json.loads(data)
    except ValueError:
        return False
    else:
        return True
