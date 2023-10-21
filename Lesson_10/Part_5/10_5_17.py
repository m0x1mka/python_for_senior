def primes(start, stop):
    for i in range(start, stop + 1):
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i
