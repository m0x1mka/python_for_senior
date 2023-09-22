def polynom(x):
    ans = x ** 2 + 1
    if not polynom.__dict__:
        polynom.__dict__["values"] = {ans}
    else:
        polynom.__dict__["values"].add(ans)
    return ans
