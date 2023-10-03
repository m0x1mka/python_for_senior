from copy import deepcopy


def get_min_max(itr):
    try:
        new_itr = deepcopy(iter(itr))
        next(new_itr)
    except Exception as e:
        print(e)
        return None
    else:
        max_itr = deepcopy(itr)
        min_itr = deepcopy(itr)
        return (min(min_itr), max(max_itr))
