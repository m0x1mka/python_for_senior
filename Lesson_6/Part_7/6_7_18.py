from collections import Counter

check_list = input().split(",")
data = Counter(check_list)
for i in sorted(data.keys()):
    ord_sum = sum([ord(j) for j in i if i != " "])
    dif = len(max(data.keys(), key=len))-len(i)
    print(f"{i + ' ' * dif}: {ord_sum} UC x {data[i]} = {ord_sum * data[i]} UC")
