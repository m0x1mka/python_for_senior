from datetime import datetime, timedelta

start = datetime.strptime(input(), '%H:%M')
times = [start]
end = datetime.strptime(input(), '%H:%M')
new_start = start
if start + timedelta(minutes=45) < end:
    while new_start < end:
        if new_start + timedelta(minutes=45) > end:
            break
        new_start += timedelta(minutes=45)
        times.append(new_start)
        new_start += timedelta(minutes=10)
        times.append(new_start)
    times = [datetime.strftime(i, '%H:%M') for i in times]
    for i in range(1, len(times), 2):
        print(f'{times[i - 1]} - {times[i]}')
