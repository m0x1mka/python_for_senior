def hide_card(card):
    card = ''.join(str(card).split())
    return '*' * 12 + card[12:]


print(hide_card("9999 9999 9999 9999"))
