from datetime import datetime, date, timedelta


def choose_plural(amount, declensions):
    rule = [(1,), (2, 3, 4), (0, *range(5, 21))]
    dct = dict(zip(rule, declensions))
    if amount > 9 and 11 <= amount % 100 <= 20:
        n = amount % 100
        for i in dct.keys():
            if n in i:
                return f'{amount} {dct[i]}'
    else:
        n = amount % 10
        for i in dct.keys():
            if n in i:
                return f'{amount} {dct[i]}'


pars = '%d.%m.%Y'
pr = '%H:%M'
date_inp = input().split()
date_sys = datetime(year=2022, month=11, day=8, hour=12)
date_com = datetime.combine(datetime.strptime(date_inp[0], pars).date(), datetime.strptime(date_inp[1], pr).time())
if date_com >= date_sys:
    print('Курс уже вышел!')
else:
    val = date_sys - date_com
    result = [val.days, val.seconds // 3600, (val.seconds // 60) % 60]
    data_day = [('день', 'дня', 'дней'), ('час', 'часа', 'часов'), ('минута', 'минуты', 'минут')]
    comb = list(zip(result, data_day))
    end = []
    for pair in comb:
        if pair[0] != 0:
            end.append(choose_plural(*pair))
    if len(end) == 3:
        del (end[2])
    print('До выхода курса осталось: ', end='')
    print(f'{end[0]} и {end[1]}' if len(end) == 2 else f'{end[0]}')
