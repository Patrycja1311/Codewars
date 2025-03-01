import math


def digits_average(x):
    digits = list(map(int, str(x)))
    while len(digits) > 1:
        digits = [math.ceil(sum(digits[i:i+2]) / 2) for i in range(len(digits) - 1)]
    return digits[0]
