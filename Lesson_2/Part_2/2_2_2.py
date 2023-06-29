en_chars = "AaBCcEeHKMOoPpTXxy"
ru_chars = "АаВСсЕеНКМОоРрТХху"
letters = [input() in en_chars for _ in range(3)]
if all(letters):
    print("en")
elif any(letters):
    print("mix")
else:
    print("ru")
