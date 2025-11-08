import math


def sort_by_area(seq):
    return sorted(seq, key=lambda x: math.pi * x ** 2 if isinstance(x, (int, float)) else x[0] * x[1])
