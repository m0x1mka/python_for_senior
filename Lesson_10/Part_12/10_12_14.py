from collections import namedtuple, defaultdict
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

dct = {}
max_mass = int(input())
items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]
for i in range(len(items) + 1):
    for i in itertools.combinations(items, r=i):
        summ = 0
        for j in i:
            summ += j.mass
        if summ < max_mass:
            dct[summ] = list(i)
max_dct = {}
for i, j in dct.items():
    summa = 0
    for k in j:
        summa += k.price
    max_dct[summa] = j
if max_dct[list(max_dct.keys())[-1]] != []:
    for i in sorted(max_dct[max(list(max_dct.keys()))], key=lambda x: x.name):
        print(i.name)
else:
    print("Рюкзак собрать не удастся")
