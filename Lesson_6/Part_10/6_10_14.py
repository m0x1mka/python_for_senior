from collections import ChainMap


def deep_update(chainmap, key, value):
    key_in_map = False
    for i in range(len(chainmap.maps)):
        if key in chainmap.maps[i].keys():
            chainmap.maps[i][key] = value
            key_in_map = True
    if not key_in_map:
        chainmap.maps[0].update({key: value})
    return None
