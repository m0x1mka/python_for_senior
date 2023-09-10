def print_digits(num):
    if num != 0:
        print_digits(num // 10)
        print(num % 10)
