import sys

lst = [int(i.strip()) for i in sys.stdin.readlines()]
if len(lst) % 2 == 0:
    print("Дима" if lst[-1] % 2 == 0 else "Анри")
else:
    print("Анри" if lst[-1] % 2 == 0 else "Дима")
