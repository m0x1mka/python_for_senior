from itertools import islice


def take_nth(itr, n):
    try:
        return next(islice(itr, n - 1, n))
    except:
        return None
