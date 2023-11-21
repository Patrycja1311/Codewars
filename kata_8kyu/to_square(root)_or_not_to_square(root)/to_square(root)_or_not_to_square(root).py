import math


def square_or_square_root(arr):
    return [math.isqrt(num) if math.isqrt(num) ** 2 == num else num ** 2 for num in arr]
