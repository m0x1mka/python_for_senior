def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return dict(enumerate(matrix, start=1))
