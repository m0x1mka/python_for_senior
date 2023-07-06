import time


def get_the_fastest_func(funcs, arg):
    times = {}
    for i in funcs:
        start = time.monotonic()
        i(arg)
        end = time.monotonic()
        times[end - start] = i
    return times[min(times.keys())]
