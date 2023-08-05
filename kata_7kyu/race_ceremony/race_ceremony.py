from math import ceil


def race_podium(blocks):
    first = ceil((blocks) / 3) + 1
    second = min(first - 1, blocks - first - 1)
    third = blocks - first - second
    return second, first, third
