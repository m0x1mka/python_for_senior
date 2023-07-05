from datetime import date, time, datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

total_minutes = 0
for i in data:
    min1 = datetime.strptime(i[0], '%H:%M')
    min2 = datetime.strptime(i[1], '%H:%M')
    period = min2.minute + min2.hour * 60 - (min1.minute + min1.hour * 60)
    total_minutes += period
print(total_minutes)
