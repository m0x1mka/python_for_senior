def linear(lst):
    final = []
    if len(lst) == 0:
        return 0
    else:
        for i in lst:
            if type(i) == list:
                final.extend(linear(i))
            else:
                final.append(i)
    return final
