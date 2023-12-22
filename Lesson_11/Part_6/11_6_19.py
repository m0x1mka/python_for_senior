import re

l = input()
print(True if re.match(r'Здравствуйте|Доброе утро|Добрый день|Добрый вечер', l, re.IGNORECASE) else False)
