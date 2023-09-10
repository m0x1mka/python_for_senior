def number_of_frogs(year):
    if year == 1:
        return 77
    return 3 * ((number_of_frogs(year - 1) if year > 2 else 77) - 30)
