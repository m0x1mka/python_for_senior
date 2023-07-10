import sys
from datetime import datetime

lst = [datetime.strptime(i.strip(), '%d.%m.%Y') for i in sys.stdin.readlines()]
if list(sorted(set(lst))) == lst:
    print("ASC")
elif list(sorted(set(lst), reverse=True)) == lst:
    print("DESC")
else:
    print("MIX")
