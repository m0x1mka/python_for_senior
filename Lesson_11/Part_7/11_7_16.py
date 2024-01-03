import re
import sys

pattern = r'<a href="(.*?)">(.*?)</a>'
texts = sys.stdin.readlines()

for text in texts:
    for link in re.findall(pattern, text):
        print(f"{link[0]}, {link[1]}")
