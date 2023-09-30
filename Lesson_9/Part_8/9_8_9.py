import functools


def square(func):
    @functools.wraps(func)
    def decorate(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return decorate
