from collections import OrderedDict


def solve(arr):
    return list(OrderedDict.fromkeys(arr[::-1]))[::-1]
