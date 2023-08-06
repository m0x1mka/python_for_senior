from zipfile import ZipFile
import os.path

file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile("4_5_20_answer.zip", mode="w") as zip_w:
    for i in file_names:
        if os.path.getsize(i) <= 100:
            zip_w.write(i)
