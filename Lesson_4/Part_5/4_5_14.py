from zipfile import ZipFile

with ZipFile("4_5_14_data.zip") as zip_data:
    count = 0
    for i in ZipFile.infolist(zip_data):
        if not i.is_dir():
            count += 1
    print(count)