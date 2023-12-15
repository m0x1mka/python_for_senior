import sys
import re
data = [line.strip() for line in sys.stdin.readlines()]
for i in data:
    print(True if re.fullmatch(r'_\d+[a-zA-Z]*_?', i)is not None else False)