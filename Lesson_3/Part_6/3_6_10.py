import time


def calculate_it(func, *args):
    start = time.monotonic()
    ans = func(*args)
    end = time.monotonic()
    return ans, end - start
