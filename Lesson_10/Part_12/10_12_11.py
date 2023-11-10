from itertools import permutations

data = input()
for i in sorted(set(permutations(list(data), r=len(data)))):
    print("".join(i))
