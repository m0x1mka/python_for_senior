from datetime import date

n = int(input())
dates = sorted([date.fromisoformat(input()) for _ in range(n)])
for i in dates:
    print(i.strftime("%d/%m/%Y"))
