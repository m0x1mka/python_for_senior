import re


def abbreviate(s):
    data = re.findall(r'\b[a-zA-Z]|[A-Z]', s)
    return ''.join(data).upper()
