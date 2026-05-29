def fraction(a, b):
    from math import gcd
    g = gcd(a, b)
    return a // g + b // g
