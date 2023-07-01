from datetime import date

date1 = date.fromisoformat(input())
date2 = date.fromisoformat(input())

final_date = min([date1, date2])
print(final_date.strftime("%d-%m (%Y)"))
