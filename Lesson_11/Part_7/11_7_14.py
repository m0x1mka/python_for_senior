import re

w = input()
t = input()

print(len(re.findall(fr'\b{w[:-3]}o[u]?r\b', t, re.IGNORECASE)))
