def new_print(func):
    def decorate(*args, **kwargs):
        new_args = [i.upper() if type(i) == str else str(i).upper() for i in args]
        new_kwargs = {k: v.upper() if type(v) == str else str(v).upper() for k, v in kwargs.items()}
        func(*new_args, **new_kwargs)

    return decorate


print = new_print(print)
