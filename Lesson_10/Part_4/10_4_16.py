class Xrange:
    def __init__(self, start, end, step=1):
        self.end = end
        self.step = step
        self.start = start - self.step  # чтоб не было проблем в методе __next__
        if self.start + self.step < self.end:  # проверям больше ли стартовое значение, чем конечное или нет
            self.default = True
        else:
            self.default = False

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.default:
            while self.start < self.end:
                return self.start
        else:
            while self.end < self.start:
                return self.start
        raise StopIteration
