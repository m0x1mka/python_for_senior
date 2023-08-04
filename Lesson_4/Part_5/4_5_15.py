from zipfile import ZipFile

with ZipFile("4_5_15_data.zip") as zip_data:
    not_compressed = 0
    compressed = 0
    for i in zip_data.infolist():
        not_compressed += i.file_size
        compressed += i.compress_size
    print(f"Объем исходных файлов: {not_compressed} байт(а)")
    print(f"Объем сжатых файлов: {compressed} байт(а)")