import sys
import re

data = [line.strip() for line in sys.stdin]
for i in data:
    match = re.search(r'(?P<Кодстраны>\d{1,3})[ -](?P<Кодгорода>\d{1,3})[ -](?P<Номер>\d{4,10})', i)
    a = match.groupdict()
    b = list(a.keys())
    print(f'{b[0][:3]} {b[0][3:]}: {a[b[0]]}, {b[1][:3]} {b[1][3:]}: {a[b[1]]}, {b[2]}: {a[b[2]]}')
