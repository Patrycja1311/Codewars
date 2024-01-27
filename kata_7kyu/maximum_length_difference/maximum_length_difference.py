def mxdiflg(a1, a2):
    return max([abs(len(x) - len(y)) for x in a1 for y in a2], default=-1)
