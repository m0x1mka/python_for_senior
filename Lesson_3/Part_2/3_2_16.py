from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
    except ValueError:
        return "Некорректная"
    else:
        return "Корректная"


counter = 0
while True:
    a = input()
    if a == "end":
        break
    day, month, year = map(int, a.split('.'))
    ans = is_correct(day, month, year)
    if ans == "Корректная":
        counter += 1
    print(ans)
print(counter)
