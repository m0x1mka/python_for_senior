from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

for i in list(data.keys())[::-1]:
    data.move_to_end(i, last=True)

print(data)
