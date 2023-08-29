from collections import Counter


check_list = input().split(",")
data = Counter(check_list)
for i in sorted(data.keys()):
    print(f"{i}: {data[i]}")
