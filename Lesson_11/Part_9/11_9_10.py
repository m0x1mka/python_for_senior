import re

s = input()
print(*re.split(r'\s*[,;.]\s*', s))
