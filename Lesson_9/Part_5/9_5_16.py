def power(degree):
    def inner(num):
        return num ** degree

    return inner
