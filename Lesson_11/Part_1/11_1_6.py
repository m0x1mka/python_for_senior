import re

n = input()
data1 = re.findall("7-\d{3}-\d{3}-\d{2}-\d{2}", n)
data2 = re.findall("8-\d{3}-\d{4}-\d{4}", n)
data = data1 + data2
print(*data, sep="\n")
