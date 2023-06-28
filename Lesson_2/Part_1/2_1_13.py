def spell(*words):
    words = [i.lower() for i in words]
    dct = {i[0]: [j for j in words if i[0] == j[0]] for i in words}
    new_dct = {i: len(max(j, key=len)) for i, j in dct.items()}
    return new_dct


used_words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*used_words))
