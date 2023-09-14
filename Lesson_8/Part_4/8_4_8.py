def dict_travel(dicts, ans=""):
    for key, value in sorted(dicts.items()):
        if isinstance(value, dict):
            dict_travel(value, ans + f"{key}.")
        else:
            print(f"{ans}{key}: {value}")