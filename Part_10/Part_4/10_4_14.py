from random import randint


class RandomNumbers:
    def __init__(self, start, stop, n):
        self.start = start
        self.stop = stop
        self.n = n
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > self.n:
            raise StopIteration
        num = randint(self.start, self.stop)
        self.count += 1
        return num
