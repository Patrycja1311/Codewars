import math


def distance_between_circles(a, b):
    d = math.sqrt((a.center.x - b.center.x)**2 + (a.center.y - b.center.y)**2)
    return max(0, d - (a.radius + b.radius)) if d > abs(a.radius - b.radius) else 0
