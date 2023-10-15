class Alphabet:
    def __init__(self, lang):
        self.lang = lang
        self.lrus = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.leng = 'abcdefghijklmnopqrstuvwxyz'
        self.ru_count = 0
        self.en_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.lang == "ru":
            if self.ru_count >= len(self.lrus):
                self.ru_count = 0
            ans = self.lrus[self.ru_count]
            self.ru_count += 1
            return ans
        else:
            if self.en_count >= len(self.leng):
                self.en_count = 0
            ans = self.leng[self.en_count]
            self.en_count += 1
            return ans
