import math


def squares_needed(grains):
    return 0 if grains == 0 else math.ceil(math.log2(grains + 1))
