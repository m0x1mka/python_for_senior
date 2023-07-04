from datetime import datetime, timedelta

today = datetime.strptime(input(), '%d.%m.%Y')
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(datetime.strftime(yesterday, '%d.%m.%Y'), datetime.strftime(tomorrow, '%d.%m.%Y'), sep='\n')
