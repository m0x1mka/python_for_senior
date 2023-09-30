import functools


def takes(*args):
    def check(func):
        @functools.wraps(func)
        def decorate(*new_args, **kwargs):
            for i in new_args + tuple(kwargs.values()):
                if type(i) not in args:
                    raise TypeError
            ans = func(*new_args, **kwargs)
            return ans

        return decorate

    return check
