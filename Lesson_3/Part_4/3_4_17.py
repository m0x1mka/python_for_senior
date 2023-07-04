from datetime import datetime, timedelta, time

current_time = datetime.strptime(input(), '%H:%M:%S')
seconds = int(input())

final_time = datetime.fromtimestamp(current_time.timestamp() + seconds)
print(datetime.strftime(final_time, '%H:%M:%S'))
