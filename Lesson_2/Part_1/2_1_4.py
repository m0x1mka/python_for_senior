def hide_card(card):
    card = ''.join(str(card).split())
    return '*' * 12 + card[12:]


card = '905 678123 45612 56'

print(hide_card(card))
