def is_iterator(obj):
    try:
        next(obj)
    except:
        return False
    else:
        return True
