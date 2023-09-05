from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if key not in chainmap:
        return None
    if from_left:
        return chainmap[key]
    else:
        chainmap.maps = reversed(chainmap.maps)
        return chainmap[key]
