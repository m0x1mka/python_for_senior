from itertools import combinations_with_replacement

wallet = [100, 50, 20, 10, 5]

lst = []
for i in range(21):
    for j in combinations_with_replacement(wallet, r=i):
        if sum(j) == 100 and sorted(j) not in lst:
            lst.append(sorted(j))
print(len(lst))
