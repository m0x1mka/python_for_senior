def custom_isinstance(obj, typeinfo):
    if type(typeinfo) != tuple:
        return len([i for i in obj if type(i) == typeinfo])
    else:
        return len([i for i in obj if type(i) in typeinfo])
