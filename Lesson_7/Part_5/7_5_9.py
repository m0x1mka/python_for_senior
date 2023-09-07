import string

alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password):
    if len(password) < 9:
        raise LengthError
    elif not (any([i.isupper() for i in password]) and any(
        [i.islower() for i in password])) or password.isdigit() or not any(
        i in string.ascii_letters + "".join(alphabet) for i in password):
        raise LetterError
    elif not any([i.isdigit() for i in password]):
        raise DigitError
    return "Success!"


while True:
    s = input()
    try:
        ans = is_good_password(s)
    except LengthError:
        print("LengthError")
    except LetterError:
        print("LetterError")
    except DigitError:
        print("DigitError")
    else:
        print(ans)
        break