def match_arrays(v, r):
    set2 = set(r)
    return sum(1 for element in v if element in set2)
