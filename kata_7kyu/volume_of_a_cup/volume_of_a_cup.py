import numpy as np


def cup_volume(d1, d2, height):
    return round((np.pi/3) * height * ((d2/2)**2 + (d2/2)*(d1/2) + (d1/2)**2), 2)
