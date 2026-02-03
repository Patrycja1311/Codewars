def closest(lst):
    m = min(abs(x) for x in lst)
    r = {x for x in lst if abs(x) == m}
    return None if len(r) > 1 else r.pop()
