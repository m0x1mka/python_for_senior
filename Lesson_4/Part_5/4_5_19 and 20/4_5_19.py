from zipfile import ZipFile

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

for i in file_names:
    with open(i, "w") as f:
        pass

with ZipFile("files.zip", mode="w") as zip_data:
    for i in file_names:
        zip_data.write(i)
