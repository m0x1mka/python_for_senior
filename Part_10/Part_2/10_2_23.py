def starmap(func, data):
    ans = []
    for i in data:
        ans.append(func(*i))
    return ans
