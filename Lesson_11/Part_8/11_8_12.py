import re

s = input()
print(re.sub(r'\b(\w)(\w)(\w*)\b', r'\2\1\3', s))
