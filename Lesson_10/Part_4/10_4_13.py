from copy import copy


class Cycle:
    def __init__(self, it):
        self.count = 0
        self.it = it

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.it):
            self.count = 0
        ans = self.it[self.count]
        self.count += 1
        return ans
