import functools


def repeat(times):
    def count_funcs(func):
        @functools.wraps(func)
        def repeat_inner(*args, **kwargs):
            for _ in range(times):
                ans = func(*args, **kwargs)
            return ans

        return repeat_inner

    return count_funcs
