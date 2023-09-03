from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

s = input().split(",")
food = Counter(s)
prices = ChainMap(bread, meat, sauce, vegetables, toppings)

total_price = 0
max_len_s = 0
max_len = len(max(s, key=len))
print(max_len)
for i in sorted(food.keys()):
    st = f'{i}{" " * (max_len  - len(i) + 1)} x {food[i]}'
    if len(st) > max_len_s:
        max_len_s = len(st)
    total_price += prices[i]
    print(st)

print(max_len_s)