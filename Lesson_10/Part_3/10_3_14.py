def is_iterable(obj):
    try:
        iter(obj)
    except:
        return False
    else:
        return True
