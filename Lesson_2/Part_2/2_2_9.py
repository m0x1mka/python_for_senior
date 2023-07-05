def translate_to_bytes(data_size, data_ext):
    if data_ext == 'B':
        return data_size
    elif data_ext == 'KB':
        data_size *= 1024
    elif data_ext == 'MB':
        data_size *= 1024 ** 2
    else:
        data_size *= 1024 ** 3
    return data_size


with open('files.txt', encoding='utf-8') as f:
    sizes_ext = {1024: 'KB', 1024 ** 2: 'MB', 1024 ** 3: 'GB'}
    lst = f.readlines()
    dict_files = {}
    for i in sorted(lst, key=lambda x: x[x.find('.') + 1: x.find(' ')]):
        extension = i[i.find('.') + 1: i.find(' ')]
        if extension not in dict_files.keys():
            dict_files[extension] = [i.strip()]
        else:
            dict_files[extension].append(i.strip())
    for i in dict_files.items():
        key = i[0]
        total_size = 0
        for j in i[1]:
            size = j[j.find(' '):]
            size = size.split()
            size[0] = int(size[0])
            total_size += translate_to_bytes(size[0], size[1])
        old_size = total_size
        while total_size % 1024 == 0:
            total_size //= 1024
        if total_size // 1024 == 0:
            dict_files[key].append('----------')
            dict_files[key].append(f'Summary: {total_size} {sizes_ext[old_size // total_size]}')
        else:
            not_rounded = total_size // 1024
            decimal_num = total_size % 1024
            if decimal_num >= 512:
                rounded = not_rounded + 1
            else:
                rounded = not_rounded
            dict_files[key].append('----------')
            dict_files[key].append(f'Summary: {rounded}' + sizes_ext[old_size * 1024 // total_size])

for i in dict_files.values():
    for j in i:
        print(j)
    print('', sep='\n')
