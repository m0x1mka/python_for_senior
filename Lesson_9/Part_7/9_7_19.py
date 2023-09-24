def sandwich(func):
    def inner(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        ans = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return ans

    return inner
