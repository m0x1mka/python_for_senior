import sys

data = [i.strip() for i in sys.stdin.readlines()]


def reverse_func(lst):
    if len(lst) > 0:
        print(lst.pop(-1))
        reverse_func(lst)


reverse_func(data)
