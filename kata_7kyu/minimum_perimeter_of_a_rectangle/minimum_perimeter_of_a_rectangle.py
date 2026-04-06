import math


def minimum_perimeter(area):
    for h in range(int(math.sqrt(area)), 0, -1):
        if area % h == 0:
            w = area // h
            return 2 * (h + w)
