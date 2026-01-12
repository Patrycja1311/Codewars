from math import gcd


def sum_differences_between_products_and_LCMs(pairs):
    return sum(
        0 if a == 0 or b == 0 else a*b - a*b//gcd(a, b)
        for a, b in pairs
    )
