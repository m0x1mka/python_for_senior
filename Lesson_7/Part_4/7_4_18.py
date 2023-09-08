import calendar
import locale


def get_weekday(number):
    if type(number) != int:
        raise TypeError('Аргумент не является целым числом')
    elif number not in range(1, 8):
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
    days = [d.title() for d in calendar.day_name]
    return days[number - 1]
