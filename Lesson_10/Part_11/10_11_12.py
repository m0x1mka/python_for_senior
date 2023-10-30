from itertools import groupby

s = input().split()
for i, j in groupby(sorted(s, key=len), key=lambda x: len(x)):
    print(f"{i} -> ", end="")
    print(*sorted(j), sep=", ")
