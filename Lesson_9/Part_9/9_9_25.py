from functools import lru_cache


@lru_cache
def ways(stairs):
    if stairs < 4:
        return 1
    if stairs == 4:
        return 2
    else:
        return ways(stairs - 1) + ways(stairs - 3) + ways(stairs - 4)
