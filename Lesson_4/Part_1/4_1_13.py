import sys

pupils = [int(i) for i in sys.stdin.readlines()]
if pupils:
    print(f"Рост самого низкого ученика: {min(pupils)}")
    print(f"Рост самого высокого ученика: {max(pupils)}")
    print(f"Средний рост: {sum(pupils) / len(pupils)}")
else:
    print("нет учеников")
