import sys

ans = sys.stdin.readlines()
for i in ans:
    i = i.strip()
    print(i[::-1])
