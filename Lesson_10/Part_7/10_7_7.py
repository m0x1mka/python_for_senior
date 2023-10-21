def filter_names(names, char, max_names):
    del_names = filter(lambda x: not x.lower().startswith(char.lower()), names)
    sorted_names = list(filter(lambda x: all([i.isalpha() for i in x]), del_names))
    for i in range(max_names):
        try:
            yield sorted_names[i]
        except:
            break
