import sys, re

data = [line.strip() for line in sys.stdin.readlines()]
summa = 0
for i in data:
    if re.search(r'.*beegeek.*', i, re.IGNORECASE):
        summa += 1

print(summa)
