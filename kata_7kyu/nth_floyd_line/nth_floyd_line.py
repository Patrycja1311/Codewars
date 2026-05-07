import math


def nth_floyd(n):
    return math.ceil((math.sqrt(8*n + 1) - 1) / 2)

