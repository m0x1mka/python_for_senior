from collections import Counter

s = input().lower()
data = Counter(s.split())
minimal = max(data.items(), key=lambda x: x[1])[1]
elements = []
for i in data.items():
    if i[1] == minimal:
        elements.append(i[0])

print(max(elements))
