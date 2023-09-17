f = input()
num_range = list(map(int, input().split()))
values = []
for x in range(num_range[0], num_range[1]+1):
    values.append(eval(f))
print(f"Минимальное значение функции {f} на отрезке [{num_range[0]}; {num_range[1]}] равно {min(values)}")
print(f"Максимальное значение функции {f} на отрезке [{num_range[0]}; {num_range[1]}] равно {max(values)}")