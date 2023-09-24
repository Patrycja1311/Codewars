import math


def gps(s, x):
    return 0 if len(x) <= 1 else math.floor(max(3600 * (x[i] - x[i-1]) / s for i in range(1, len(x))))
