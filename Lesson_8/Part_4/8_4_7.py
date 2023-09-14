def get_all_values(dicts, key):
    values = set()
    if key in dicts:
        values.add(dicts[key])
    for d in dicts.values():
        if type(d) == dict:
            ans = get_all_values(d, key)
            if ans is not None:
                values.update(ans)
    return values


