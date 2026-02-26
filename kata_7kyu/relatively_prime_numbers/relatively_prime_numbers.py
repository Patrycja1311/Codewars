import math


def relatively_prime(n, lst):
    result = []
    for number in lst:
        if math.gcd(n, number) == 1:
            result.append(number)
    return result
