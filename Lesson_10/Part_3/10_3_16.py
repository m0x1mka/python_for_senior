from random import randint


def random_numbers(start, stop):
    return iter(lambda: randint(start, stop), stop + 1)
