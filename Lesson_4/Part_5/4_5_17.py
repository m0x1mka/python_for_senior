from zipfile import ZipFile
from datetime import datetime

with ZipFile("lesson_data.zip") as zip_data:
    lst = []
    for i in ZipFile.infolist(zip_data):
        a = i.date_time
        if datetime.strptime(f"{a[0]}-{a[1]}-{a[2]} {a[3]}:{a[4]}:{a[5]}", "%Y-%m-%d %H:%M:%S") > datetime.strptime(
                "2021-11-30 14:22:00",
                "%Y-%m-%d %H:%M:%S"):
            lst.append(i)
    for i in sorted(lst, key=lambda x: x.filename):
        if not i.is_dir():
            ans = i.filename
            print(ans[ans.index("/")+1:] if "/" in ans else ans)
