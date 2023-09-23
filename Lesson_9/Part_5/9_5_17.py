def generator_square_polynom(a, b, c):
    def make_pol(x):
        return a * x ** 2 + b * x + c

    return make_pol
