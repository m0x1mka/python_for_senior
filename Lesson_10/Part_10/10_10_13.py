def sum_of_digits(itr):
    return sum(map(lambda x: sum([int(i) for i in str(x)]), itr))
