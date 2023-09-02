from collections import Counter

s = input().lower()
data = Counter([len(i) for i in s.split()])
for i in sorted(data.items(), key=lambda x: x[1]):
    print(f"Слов длины {i[0]}: {i[1]}")

