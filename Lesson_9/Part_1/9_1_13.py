def my_pow(num):
    summ = 0
    for i in str(num):
        summ += int(i) ** (str(num).index(i) + 1)
    return summ
