def choose_plural(amount, declensions):
    num = int(str(amount)[-1])
    if num >= 5 or (amount > 10 and int(str(amount)[-2:]) in (11, 12, 13, 14)):
        num = 3
    elif num in [2, 3, 4]:
        num = 2
    return str(amount) + " " + str(declensions[num - 1])


print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
