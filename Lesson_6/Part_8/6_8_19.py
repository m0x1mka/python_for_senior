from collections import Counter


def scrabble(symbols, word):
    return Counter(symbols) > Counter(word)
