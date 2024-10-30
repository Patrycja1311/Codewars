from math import floor


def sum_average(arr):
    return floor(sum(sum(sub_arr) / len(sub_arr) for sub_arr in arr))
