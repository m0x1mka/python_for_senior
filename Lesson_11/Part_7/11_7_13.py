import re

w = input()
t = input()
print(len(re.findall(fr'\b{w[:-2]}[sz]e\b', t, re.IGNORECASE)))
