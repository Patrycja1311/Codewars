def max_sum_between_two_negatives(arr):
    m, s = -1, None
    for x in arr:
        if x < 0:
            if s != None: m = max(m, s)
            s = 0
            continue
        if s != None: s += x
    return m
