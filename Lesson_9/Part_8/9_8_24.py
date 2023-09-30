import functools


def ignore_exception(*args):
    def make_exceptions(func):
        @functools.wraps(func)
        def decorate(*new_args, **kwargs):
            try:
                func(*new_args, **kwargs)
            except Exception as e:
                name_exc = type(e).__name__
                if name_exc in [i.__name__ for i in args]:
                    print(f"Исключение {name_exc} обработано")
                else:
                    raise e
            else:
                return func(*new_args, **kwargs)

        return decorate

    return make_exceptions
    