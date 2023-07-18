import csv

with open("4_2_22.csv", encoding="utf-8") as f:
    prices = list(csv.DictReader(f, delimiter=";"))
    for i in range(len(prices)):
        for j in prices[i].keys():
            if prices[i][j].isdigit():
                prices[i][j] = int(prices[i][j])
    new_prices = {}
    for i in range(len(prices)):
        minimal = (0, 1000)
        for j in prices[i].items():
            if type(j[1]) == int:
                if j[1] < minimal[1]:
                    minimal = j
        new_prices[prices[i]["Магазин"]] = minimal
    the_most_minimal = [0, [0, 1000]]
    for i in new_prices.items():
        if i[1][1] < the_most_minimal[1][1]:
            the_most_minimal = i
    print(f"{the_most_minimal[1][0]}: {the_most_minimal[0]}")
