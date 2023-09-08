import json

file = input()
try:
    with open(file) as f:
        try:
            data = json.load(f)
        except ValueError:
            print("Ошибка при десериализации")
        else:
            print(data)
except FileNotFoundError:
    print("Файл не найден")
