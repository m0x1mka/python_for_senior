def card_deck(suit):
    count1 = ['пик', 'треф', 'бубен', 'червей']
    count2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'валет', 'дама', 'король', 'туз']
    while True:
        for i in count1:
            if i == suit:
                continue
            for j in count2:
                yield str(j) + " " + i
