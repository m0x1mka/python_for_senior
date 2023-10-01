from functools import lru_cache


@lru_cache
def sort_word(word):
    return "".join(sorted([i for i in word]))


while True:
    try:
        a = input()
    except:
        break
    else:
        print(sort_word(a))
