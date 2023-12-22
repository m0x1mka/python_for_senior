import sys, re

data = [line.strip() for line in sys.stdin.readlines()]
summa = 0
for i in data:
    if re.fullmatch(r'\bbeegeek.*beegeek\b', i):
        summa += 3
    elif re.fullmatch(r'(\bbeegeek.*\b)|(\b.*beegeek\b)', i):
        summa += 2
    elif re.search(r'.*beegeek.*', i):
        summa += 1
print(summa)
