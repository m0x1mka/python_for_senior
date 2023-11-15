from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
lst = []
for i in range(len(wallet)):
    for i in combinations(wallet, r=i):
        if sorted(i) not in lst and sum(i) == 100:
            lst.append(sorted(i))
print(len(lst))
