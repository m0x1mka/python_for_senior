from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

num = len(data.items())
new_data = OrderedDict()

for i in range(num):
    ans = data.popitem(last=(i % 2 == 1))
    new_data.update({ans[0]: ans[1]})

print(new_data)
