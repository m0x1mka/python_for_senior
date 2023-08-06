from zipfile import ZipFile
from datetime import datetime

with ZipFile("lesson_data.zip") as zip_data:
    for i in sorted(ZipFile.infolist(zip_data),
                    key=lambda x: x.filename[x.filename.index("/") + 1:] if "/" in x.filename else x.filename):
        if not i.is_dir():
            ans = i.filename
            a = i.date_time
            print(ans[ans.find("/") + 1:] if "/" in ans else ans)
            print(
                f"  Дата модификации файла: {datetime.strptime(f'{a[0]}-{a[1]}-{a[2]} {a[3]}:{a[4]}:{a[5]}','%Y-%m-%d %H:%M:%S')}")
            print(f"  Объем исходного файла: {i.file_size} байт(а)")
            print(f"  Объем сжатого файла: {i.compress_size} байт(а)\n")
