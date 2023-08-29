from collections import Counter

s = input().lower()
data = Counter(s.split())
print(data.most_common()[0][0])
