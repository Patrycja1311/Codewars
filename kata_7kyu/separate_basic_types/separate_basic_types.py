def separate_types(seq):
    res = {}
    for x in seq:
        t = bool if isinstance(x, bool) else type(x)
        res.setdefault(t, []).append(x)
    return res
