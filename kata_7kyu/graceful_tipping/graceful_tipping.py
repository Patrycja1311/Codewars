import math


def graceful_tipping(bill):
    total = bill * 1.15
    magnitude = 1 if total < 10 else 5 * 10 ** (len(str(int(total))) - 2)
    return math.ceil(total / magnitude) * magnitude
