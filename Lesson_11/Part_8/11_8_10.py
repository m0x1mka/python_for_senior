import re


def normalize_whitespace(s):
    return re.sub(r'\s+', r' ', s)
