a = input()
b = eval(a)
if type(b) == list:
    print(b[-1])
elif type(b) == set:
    print(len(b))
else:
    print(b[0])
