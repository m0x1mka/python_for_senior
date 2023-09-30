import functools


def add_attrs(**kwargs):
    def adding(func):
        func.__dict__.update(kwargs)

        @functools.wraps(func)
        def decorate(*args, **new_kwargs):
            return func(*args, **new_kwargs)

        return decorate

    return adding
