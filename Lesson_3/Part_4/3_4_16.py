from datetime import datetime, timedelta

current_time = input()
times_lst = list(map(int, current_time.split(':')))
print(times_lst[0] * 3600 + times_lst[1] * 60 + times_lst[2])
