def palindromes():
    count = 1
    while True:
        if str(count) == str(count)[::-1]:
            yield count
        count += 1
