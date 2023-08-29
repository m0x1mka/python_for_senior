from collections import Counter

s = input().lower()
data = Counter(s.split())
minimal = sorted([i[0] for i in data.most_common() if i[1] == min(data.most_common(), key=lambda x: x[1])[1]])
print(", ".join(minimal))
