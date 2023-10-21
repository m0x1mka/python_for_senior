class CardDeck:
    def __init__(self):
        self.count = 0
        self.cards = [f'{j} {i}' for i in ("пик", "треф", "бубен", "червей") for j in
                      ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 52:
            raise StopIteration
        card = self.cards[self.count]
        self.count += 1
        return card
