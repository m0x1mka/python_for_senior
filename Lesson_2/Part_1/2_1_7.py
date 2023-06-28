def print_given(*args, **kwargs):
    for i in args:
        print(f"{i} {type(i)}")
    lst = []
    for i, j in kwargs.items():
        lst.append((i, j))
    lst.sort()
    for i in lst:
        print(f"{i[0]} {i[1]} {type(i[1])}")


print_given(b=2, d=4, c=3, a=1)
