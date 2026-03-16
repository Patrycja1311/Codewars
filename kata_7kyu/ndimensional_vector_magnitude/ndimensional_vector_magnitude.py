import math


def magnitude(vector):
    return math.sqrt(sum(x*x for x in vector))
