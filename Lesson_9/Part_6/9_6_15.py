def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    max_mark = max(grades["grades"])
    del grades["grades"]
    grades["top_grade"] = max_mark
    return grades


print(*top_grade.__annotations__.values())
