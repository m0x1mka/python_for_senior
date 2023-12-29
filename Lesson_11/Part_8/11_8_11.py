import keyword
import re

s = input()
print(re.sub(fr'{"|".join(sorted(keyword.kwlist, key=len, reverse=True))}', r'<kw>', s, flags=re.IGNORECASE))
