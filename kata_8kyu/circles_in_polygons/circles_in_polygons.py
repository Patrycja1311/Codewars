import math


def circle_diameter(sides, side_length):
    if sides < 3:
        raise ValueError("Polygon must have at least 3 sides.")

    diameter = side_length / math.tan(math.pi / sides)
    return diameter
