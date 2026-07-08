from math import sqrt


def stack_height_2d(layers):
    return 0 if layers == 0 else 1 + (layers - 1) * sqrt(3) / 2

