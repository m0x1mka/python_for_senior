def get_pow(num, pow):
    if pow == 0:
        return 1
    return num * get_pow(num, pow - 1)
