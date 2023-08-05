from zipfile import ZipFile

with ZipFile("4_5_16_data.zip") as zip_data:
    sizes = {}
    for i in ZipFile.infolist(zip_data):
        if not i.is_dir():
            percentage = 100 - (i.compress_size/i.file_size) * 100
            sizes[percentage] = i.filename
    ans = sizes[max(list(sizes.keys()))]
    print(ans[ans.index("/")+1:])
