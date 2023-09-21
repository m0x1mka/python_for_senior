import string


def verification(login, password, success, failure, msg=""):
    if not any([i in string.ascii_letters for i in password]):
        msg = "в пароле нет ни одной буквы"
    elif not any([i.isupper() and i in string.ascii_uppercase for i in password]):
        msg = "в пароле нет ни одной заглавной буквы"
    elif not any([i.islower() and i in string.ascii_lowercase for i in password]):
        msg = "в пароле нет ни одной строчной буквы"
    elif not any([i.isdigit() for i in password]):
        msg = "в пароле нет ни одной цифры"
    if msg:
        return failure(login, msg)
    else:
        return success(login)
