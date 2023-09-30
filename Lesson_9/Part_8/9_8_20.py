import functools


def strip_range(start, end, char="."):
    def string_func(func):
        @functools.wraps(func)
        def decorate(*args, **kwargs):
            value = func(*args, **kwargs)
            result = value[:start] + len(value[start:end]) * char + value[end:]
            return result

        return decorate

    return string_func
