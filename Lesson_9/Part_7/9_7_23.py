def exception_decorator(func):
    def decorate(*args, **kwargs):
        try:
            ans = func(*args, **kwargs)
        except:
            return (None, "При вызове функции произошла ошибка")
        else:
            return (ans, 'Функция выполнилась без ошибок')

    return decorate
