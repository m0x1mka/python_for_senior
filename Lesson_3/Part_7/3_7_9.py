import calendar

d = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
data = list(map(int, input().split('-')))
ans = calendar.weekday(data[0], data[1], data[2])
print(d[ans + 1])
