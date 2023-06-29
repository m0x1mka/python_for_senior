n = int(input())
langs = []
for _ in range(n):
    langs.append(set(input().split(', ')))
while len(langs) != 1:
    langs[1] = langs[0] & langs[1]
    del langs[0]
print(', '.join(sorted(*langs)) if langs[0] else "Сериал снять не удастся")
