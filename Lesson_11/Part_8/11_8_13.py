import re


def rec_func(s):
    if "(" not in s:
        return s
    new = re.findall(r"([a-z]*)(\d+)\((\w+)\)(.*)", s)
    num = int(new[0][1])
    ss = new[0][2]
    if num != 0:
        s = re.sub(r"([a-z]*)(\d+)\((\w+)\)(.*)", fr"\1{ss * (num)}\4", s)
    else:
        s = re.sub(r"([a-z]*)(\d+)\((\w+)\)(.*)", r"\1\4", s)
    return rec_func(s)


s = input()
print(rec_func(s))
