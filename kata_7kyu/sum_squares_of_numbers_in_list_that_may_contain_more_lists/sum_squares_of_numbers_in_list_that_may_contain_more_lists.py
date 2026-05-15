def sumsquares(lst):
    return sum(sumsquares(x) if isinstance(x, list) else x*x for x in lst)
