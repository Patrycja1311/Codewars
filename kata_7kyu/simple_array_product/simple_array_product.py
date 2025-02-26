from itertools import product


def solve(arr):
    return max(map(lambda x: eval('*'.join(map(str, x))), product(*arr)))
