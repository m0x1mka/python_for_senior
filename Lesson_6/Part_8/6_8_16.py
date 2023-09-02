import sys
from collections import Counter

data = [i.strip().split() for i in sys.stdin.readlines()]
print(sorted(data, key=lambda x: int(x[1]))[1][0])