import math


def nearest_sq(n):
    if type(math.sqrt(n)) == int:
        return n
    else:
        return (round(math.sqrt(n))) ** 2