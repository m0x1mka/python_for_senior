import sys

nums = [int(i) for i in sys.stdin.readlines()]


def check_progression(lst):
    counter_ar = 0
    counter_ge = 0
    for i in range(1, len(nums) - 1):
        if 2 * lst[i] == lst[i - 1] + lst[i + 1]:
            counter_ar += 1
        elif lst[i] ** 2 == lst[i - 1] * lst[i + 1]:
            counter_ge += 1
    if counter_ar == len(lst) - 2:
        return "Арифметическая прогрессия"
    elif counter_ge == len(lst) - 2:
        return "Геометрическая прогрессия"
    return "Не прогрессия"
