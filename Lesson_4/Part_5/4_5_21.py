from zipfile import ZipFile


def extract_this(zip_data, *args):
    with ZipFile(zip_data) as zip_data:
        zip_data.extractall(args or None)
