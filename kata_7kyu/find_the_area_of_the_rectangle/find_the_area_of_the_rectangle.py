from math import sqrt


def area(d, l):
    return "Not a rectangle" if d <= l else round(l * sqrt(d**2 - l**2), 2)