from math import factorial
from itertools import count


def factorials(num):
    for i in range(1, num + 1):
        yield factorial(i)
