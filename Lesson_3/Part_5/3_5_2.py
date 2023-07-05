from datetime import date

d = dict()
for Y in range(1, 10000):
    for M in range(1, 13):
        d_13 = date(Y, M, 13)
        key = d_13.isoweekday()
        if key in d.keys():
            d[key] = d[key] + 1
        else:
            d[key] = 1
for i in sorted(d.keys()):
    print(d[i])
