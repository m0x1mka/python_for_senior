import re

l = input()
w = input()
print(len(re.findall(fr'\b{w}\b', l)))
