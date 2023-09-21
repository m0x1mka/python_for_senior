def print_operation_table(func, a, b):
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print(func(i, j), end=" ")
        print()
