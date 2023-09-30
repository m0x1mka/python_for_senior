import functools


def returns(type_obj):
    def find_type(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            ans = func(*args, **kwargs)
            if type(ans) != type_obj:
                raise TypeError
            return ans

        return decorate

    return find_type
