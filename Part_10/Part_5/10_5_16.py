def alternating_sequence(count=None):
    if count is None:
        counter = 1
        while True:
            if counter % 2 == 0:
                counter = -counter
            elif counter < 0:
                counter *= -1
            yield counter
            if counter < 0:
                counter -= 1
            else:
                counter += 1
    else:
        for i in range(1, count + 1):
            if i % 2 == 0:
                i = -i
            yield i
