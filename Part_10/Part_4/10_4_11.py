class PowerOf:
    def __init__(self, num):
        self.num = num
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        ans = self.num ** self.count
        self.count += 1
        return ans
