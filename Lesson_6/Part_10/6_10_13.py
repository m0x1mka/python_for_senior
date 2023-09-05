from collections import ChainMap


def get_all_values(chainmap, key):
    keywords = set()
    for i in chainmap.maps:
        if key in i:
            keywords.add(i[key])
    return keywords

