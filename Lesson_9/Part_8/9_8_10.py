import functools


def returns_string(func):
    @functools.wraps(func)
    def decorate(*args, **kwargs):
        ans = func(*args, **kwargs)
        if type(ans) != str:
            raise TypeError
        return ans

    return decorate
