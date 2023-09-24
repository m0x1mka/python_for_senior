def do_twice(func):
    def decorate(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return decorate
