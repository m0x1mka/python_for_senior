def takes_positive(func):
    def decorate(*args, **kwargs):
        for i in list(args) + list(kwargs.values()):
            if type(i) != int:
                raise TypeError
            elif i <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return decorate
