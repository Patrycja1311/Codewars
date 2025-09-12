import math


def cooking_time(eggs):
    return 0 if eggs == 0 else math.ceil(eggs / 8) * 5
