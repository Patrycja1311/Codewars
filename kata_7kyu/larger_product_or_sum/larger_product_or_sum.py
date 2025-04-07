from math import prod


def sum_or_product(array, n):
    arr_sorted = sorted(array)
    s = sum(arr_sorted[-n:])
    p = prod(arr_sorted[:n])
    return "sum" if s > p else "product" if p > s else "same"

