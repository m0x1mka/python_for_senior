import re

s = input()
s = re.sub(r"\b(\w+)(?:\W+\1\b)+", r"\1", s)
print(s)
