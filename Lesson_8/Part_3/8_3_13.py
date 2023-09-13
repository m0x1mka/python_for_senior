def is_power(num):
    if num % 1 != 0:
        return False
    elif num == 1:
        return True
    return is_power(num / 2)
