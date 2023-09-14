def no_cycles(n):
    if n > 0:
        print(n)
        no_cycles(n - 5)
    print(n)


no_cycles(int(input()))
