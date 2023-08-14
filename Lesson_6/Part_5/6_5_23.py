from collections import defaultdict


def flip_dict(list_of_dicts):
    dct = defaultdict(list)
    for key, value in list_of_dicts.items():
        for num in value:
            dct[num].append(key)
    print(dct)
