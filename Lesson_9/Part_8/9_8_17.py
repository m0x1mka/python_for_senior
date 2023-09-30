import functools


def prefix(string, to_the_end=False):
    def add_prefix(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            ans = func(*args, **kwargs)
            if to_the_end:
                ans += string
            else:
                ans = string + ans
            return ans

        return decorate

    return add_prefix
