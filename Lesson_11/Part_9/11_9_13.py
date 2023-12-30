import re

a, b = list(map(int, input().split()))
num = re.compile(r'\d+')
s = input()
print(sum(list(map(int, num.findall(s, pos=a, endpos=b)))))
