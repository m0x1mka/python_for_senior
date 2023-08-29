from collections import Counter
import string

with open("6_7_19_data.txt", encoding="utf-8") as f:
    txt = f.read().lower()
    letters = [i for i in txt if i in string.ascii_lowercase]
    data = Counter(letters)
    for i in sorted(data.keys()):
        print(f"{i}: {data[i]}")
