class Fibonacci:
    def __init__(self):
        self.lst = [1, 1]
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < 3:
            self.count += 1
            return 1
        new = self.lst[-1] + self.lst[-2]
        self.count += 1
        self.lst.append(new)
        return new
