def distinct(seq):
    return [x for i, x in enumerate(seq) if x not in seq[:i]]
