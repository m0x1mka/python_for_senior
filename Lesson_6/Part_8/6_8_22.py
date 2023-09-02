from collections import Counter

books = Counter(input().split())
clients = int(input())
total_price = 0
for i in range(clients):
    data = input().split()
    book = data[0]
    price = int(data[1])
    if books[book] >= 1:
        total_price += price
        books[book] -= 1
print(total_price)
