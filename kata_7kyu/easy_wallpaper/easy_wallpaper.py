import math


def wallpaper(l, w, h):
    if l * w * h == 0:
        return "zero"
    total_area = 2 * (l * h + w * h)
    rolls_needed = math.ceil(total_area * 1.15 / (0.52 * 10))
    return numbers[min(rolls_needed, 20)]
