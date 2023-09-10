def sum_num(num):
    if num > 0:
        return num % 10 + sum_num(num // 10)