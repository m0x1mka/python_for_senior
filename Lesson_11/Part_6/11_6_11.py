import sys
import re

data = [line.strip() for line in sys.stdin.readlines()]
for i in data:
    lenght = len(i) // 2
    if i[:lenght] == i[lenght:]:
        print(i)
