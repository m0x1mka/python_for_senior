import re

l = input()
w = input()

print(len(re.findall(fr'\B{w}\B', l)))
