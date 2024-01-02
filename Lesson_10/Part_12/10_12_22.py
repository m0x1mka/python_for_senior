from itertools import product

n = int(input())
m = int(input())
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
current = lst[:n]

ans = product(current, repeat=m)
for i in ans:
    print("".join(i), end=" ")
