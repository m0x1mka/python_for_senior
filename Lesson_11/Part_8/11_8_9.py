import re


def normalize_jpeg(jpg):
    return re.sub(r'jpe?g$', r'jpg', jpg, flags=re.IGNORECASE)
