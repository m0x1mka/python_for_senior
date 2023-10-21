def simple_sequence():
    count = 1
    while True:
        for _ in range(count):
            yield count
        count += 1
