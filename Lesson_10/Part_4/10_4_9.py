class Square:
    def __init__(self, num):
        self.num = num
        self.edge = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.edge - self.num == 1:
            raise StopIteration
        value = self.edge ** 2
        self.edge += 1
        return value
