with open("sales.csv") as f:
    lst = [i.split(";") for i in f.readlines()]
    for i in lst[1:]:
        if int(i[2]) < int(i[1]):
            print(i[0])
