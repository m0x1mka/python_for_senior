def sandclock(num):
    if num < 4:
        print((str(num) * (5 - num) * 4).center(16))
        sandclock(num + 1)
    print((str(num) * (5 - num) * 4).center(16))


sandclock(1)
