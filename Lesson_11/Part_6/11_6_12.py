import sys
import re

data = [line.strip() for line in sys.stdin.readlines()]
a = 0
b = 0
for i in data:
    if re.fullmatch(r'.*(bee).*\1.*', i):
        a += 1
    if re.search(r'\bgeek\b', i):
        b += 1
print(a)
print(b)
