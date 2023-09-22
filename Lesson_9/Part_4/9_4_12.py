import sys

old_print = print


def new_print(*args, end="\n", sep=" "):
    lst = []
    for i in args:
        if type(i) == str:
            i = i.upper()
        lst.append(i)
    old_print(*lst, sep=sep.upper(), end=end.upper())


print = new_print
