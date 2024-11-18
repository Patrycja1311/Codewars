def one(sq, fun):
    return sum(map(fun, sq)) == 1


def bigger_than_ten(x):
    return x > 10
