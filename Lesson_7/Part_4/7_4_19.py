import string


def get_id(names, name):
    if type(name) != str:
        raise TypeError('Имя не является строкой')
    elif name[0].islower() or any([i not in string.ascii_lowercase for i in name]):
        raise ValueError('Имя не является корректным')
    return len(names) + 1
