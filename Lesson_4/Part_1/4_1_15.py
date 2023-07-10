import sys
import string

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "#", " ", ",", "."]


def check_comments(line):
    inside_count = 0
    for letter in line.strip():
        if letter in alphabet or (letter in string.ascii_letters and line.strip()[0] == '#'):
            inside_count += 1
    if inside_count == len(line.strip()) and inside_count != 0:
        return True
    return False


code = sys.stdin.read().split('\n')

for i in code:
    if not check_comments(i):
        print(i)
