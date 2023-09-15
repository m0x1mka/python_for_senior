data = input()
lst = [[] for _ in range(4)]
for i in data:
    if i.islower() and i.isalpha():
        lst[0].append(i)
    elif i.isupper() and i.isalpha():
        lst[1].append(i)
    elif not i.isalpha() and int(i) % 2 != 0:
        lst[2].append(i)
    else:
        lst[3].append(i)

print("".join(["".join(sorted(i)) for i in lst]))
