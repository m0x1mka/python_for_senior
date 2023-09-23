from collections import deque


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    dq = deque(numbers)
    dq.rotate(step)
    numbers[:] = [i for i in dq]


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)
