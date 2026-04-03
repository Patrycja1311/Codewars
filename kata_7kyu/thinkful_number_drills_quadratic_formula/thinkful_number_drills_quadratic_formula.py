import math


def quadratic_formula(a, b, c):
    discriminant = math.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return [root1, root2]
