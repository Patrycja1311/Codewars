from math import hypot


def furthest_distance(points):
    return round(max(
        hypot(a[0] - b[0], a[1] - b[1])
        for i, a in enumerate(points)
        for b in points[i+1:]
    ), 2)

