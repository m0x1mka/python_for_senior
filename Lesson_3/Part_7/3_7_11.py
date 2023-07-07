import calendar

d = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11,
     'Dec': 12}
year, month = input().split()
year = int(year)
num_month = d[month[:3]]
print(calendar.monthrange(year, num_month)[1])
