import sys

txt = sys.stdin.readlines()
word = txt[-1]
for i in sorted(sorted(txt[:-1]), key=lambda x: float(x[x.rfind('/ ') + 1:-1])):
    if word in i:
        print(i[:i.find(' /')])
