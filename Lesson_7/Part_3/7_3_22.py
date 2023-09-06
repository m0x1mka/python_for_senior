file = input()

try:
    with open(file, encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден")
