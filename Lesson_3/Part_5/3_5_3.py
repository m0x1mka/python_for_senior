from datetime import datetime

current_time = datetime.strptime(input(), '%d.%m.%Y %H:%M')
if current_time.weekday() in [5, 6] and (current_time.hour >= 18 or current_time.hour < 10):
    print('Магазин не работает')
elif current_time.hour >= 21 or current_time.hour < 9:
    print('Магазин не работает')
else:
    time_before_closing = (17 - current_time.hour) * 60 + 60 - current_time.minute
    if current_time.weekday() not in [5, 6]:
        time_before_closing += 180
    print(time_before_closing)
