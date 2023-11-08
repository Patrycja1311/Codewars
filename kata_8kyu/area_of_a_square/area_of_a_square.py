import math


def square_area(A):
    r = (360 * A)/(90 * 2 * math.pi)
    return  round(r * r, 2)
