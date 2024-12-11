import math


def is_square(arr):
    if not arr:
        return None
    return all(math.isqrt(num) ** 2 == num for num in arr)
