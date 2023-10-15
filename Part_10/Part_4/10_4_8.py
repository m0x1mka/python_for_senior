class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.times:
            raise StopIteration
        self.counter += 1
        return self.obj
