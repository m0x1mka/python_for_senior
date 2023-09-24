def reverse_args(func):
    def decorate(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return decorate
