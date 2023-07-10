import sys
from datetime import datetime

datas = [datetime.strptime(i.strip(), '%Y-%m-%d') for i in sys.stdin.readlines()]
print(datetime.toordinal(max(datas)) - datetime.toordinal(min(datas)))
