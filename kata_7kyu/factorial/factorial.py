import math


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    else:
        return math.factorial(n)
