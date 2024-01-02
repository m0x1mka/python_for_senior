import re
import sys

code = sys.stdin.read()
pattern = r'(\s*""".*?""")|(\n? *#.*?$)'

print(re.sub(pattern, '', code, flags=re.S | re.M))
