from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    new_ord = sorted(ordered_dict.items(), key=lambda x: x[1] if by_values else x[0])
    for i in new_ord:
        ordered_dict.move_to_end(i[0])
    return None


data1 = OrderedDict(e=11, b=22, a=99, g=33, c=33, d=33, h=99, f=77, i=88, k=44)
custom_sort(data1, by_values=True)

print(*data1.items())
