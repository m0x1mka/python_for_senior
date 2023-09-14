def to_binary(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return str(to_binary(n // 2)) + f"{n % 2}"
