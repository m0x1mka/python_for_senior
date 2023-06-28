def likes(users):
    if not users:
        return "Никто не оценил данную запись"
    elif len(users) == 1:
        return f"{users[0]} оценил(а) данную запись"
    elif len(users) == 2:
        return f"{users[0]} и {users[1]} оценили данную запись"
    elif len(users) == 3:
        return f"{users[0]}, {users[1]} и {users[2]} оценили данную запись"
    else:
        return f"{users[0]}, {users[1]} и {len(users[2:])} других оценили данную запись"


print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))
