import math


def coordinates(degrees: float, radius: float) -> tuple[float, float]:
    radians = math.radians(degrees)

    x = radius * math.cos(radians)
    y = radius * math.sin(radians)

    return (x, y)
