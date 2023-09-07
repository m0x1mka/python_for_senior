def is_good_password(password):
    return len(password) >= 9 and (password.upper() != password and password.lower() != password) and any(
        [i.isdigit() for i in password])
