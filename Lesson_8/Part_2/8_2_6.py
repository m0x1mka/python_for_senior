def nums(number):
    if number > 0:
        nums(number - 1)
        print(number)


nums(100)
