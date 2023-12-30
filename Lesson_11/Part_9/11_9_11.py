import re

s = input()
print(", ".join(re.split(r'\s*\|\s*|\s*&\s*|\s*and\s*|\s*or\s*', s)))
