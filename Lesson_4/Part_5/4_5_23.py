from zipfile import ZipFile


def size_for_output(size_in_bites: int) -> str:
    """Возвращает строку (для вывода) <размер еденица>"""
    if size_in_bites >= 1024 ** 3:
        return f"{str(round(size_in_bites / 1024 ** 3))} GB"
    if size_in_bites >= 1024 ** 2:
        return f"{str(round(size_in_bites / 1024 ** 2))} MB"
    if size_in_bites >= 1024:
        return f"{str(round(size_in_bites / 1024))} KB"
    return f"{str(size_in_bites)} B"


with ZipFile("4_5_23_data.zip") as zip_data:
    for i in zip_data.infolist():
        num = i.filename.count("/")
        file_name = i.filename.strip("/").split("/")[-1]
        size = size_for_output(i.file_size) if not i.is_dir() else ""
        print("  " * (num if not i.filename.endswith("/") else num - 1) + file_name + " " + size)
