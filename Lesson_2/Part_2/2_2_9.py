with open('files.txt', encoding='utf-8') as f:
    lst = f.readlines()
    dict_files
    for i in lst:
        if i[-3:] not in dict_files.keys():
            dict_files[i[-3:]] = i
    print(dict_files)





