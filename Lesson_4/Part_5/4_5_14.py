from zipfile import ZipFile

with ZipFile("lesson_data.zip") as zip_data:
    count = 0
    for i in ZipFile.infolist(zip_data):
        if not i.is_dir():
            count += 1
    print(count)