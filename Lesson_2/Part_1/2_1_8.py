def convert(text):
    lows = [i for i in text if i.islower()]
    ups = [i for i in text if i.isupper()]
    return text.lower() if len(lows) >= len(ups) else text.upper()


print(convert("ascDEF"))
