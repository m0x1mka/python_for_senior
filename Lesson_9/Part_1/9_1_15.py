def zip_longest(*data, fill=None):
    max_len = len(max(data, key=len))
    new_data = [i + [fill] * (max_len - len(i)) if len(i) < max_len else i for i in data]
    return list(zip(*new_data))
