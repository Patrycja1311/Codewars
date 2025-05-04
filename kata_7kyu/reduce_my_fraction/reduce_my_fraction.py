from math import gcd


def reduce_fraction(fraction):
    g = gcd(fraction[0], fraction[1])
    return (fraction[0] // g, fraction[1] // g)
