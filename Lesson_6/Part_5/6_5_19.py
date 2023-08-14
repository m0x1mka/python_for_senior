from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

things = defaultdict(int)
for i in data:
    if i[0] not in things.keys():
        things[i[0]] = i[1]
    else:
        things[i[0]] += i[1]

for i in sorted(things.items(), key=lambda x: x[0]):
    print(f"{i[0]}: ${i[1]}")
