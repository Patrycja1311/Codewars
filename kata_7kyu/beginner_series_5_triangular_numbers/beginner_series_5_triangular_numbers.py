import math


def is_triangular(t):
    discriminant = 1 + 8 * t
    sqrt_discriminant = int(math.sqrt(discriminant))
    if sqrt_discriminant * sqrt_discriminant != discriminant:
        return False
    n = (-1 + sqrt_discriminant) / 2
    return n.is_integer()
