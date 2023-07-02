from datetime import datetime

seconds = 2483228800
dt = datetime(2011, 11, 4)

print(datetime.fromtimestamp(float(seconds)))
print(dt.timestamp())
