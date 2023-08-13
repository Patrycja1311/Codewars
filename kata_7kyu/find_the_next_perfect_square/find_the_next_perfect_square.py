import math


def find_next_square(sq):
    sqrt_sq = math.isqrt(sq)
    if sqrt_sq * sqrt_sq == sq:
        next_int = sqrt_sq + 1
        return next_int * next_int
    else:
        return -1
