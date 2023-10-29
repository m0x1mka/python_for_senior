from collections import namedtuple, defaultdict

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons_height = defaultdict(list)
for i in persons:
    persons_height[i.height].append(i.name)

for i, j in sorted(list(persons_height.items()), key=lambda x: x[0]):
    print(i, end=": ")
    print(*sorted(j), sep=", ")