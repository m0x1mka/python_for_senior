import sys

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "#", " ", ","]
code = sys.stdin.readlines()
counter = 0
for line in code:
    inside_count = 0
    for letter in line.strip():
        if letter in alphabet:
            inside_count += 1
    if inside_count == len(line.strip()):
        counter += 1
print(counter)
