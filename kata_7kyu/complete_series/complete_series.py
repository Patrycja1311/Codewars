def complete_series(seq):
    return [0] if len(seq) != len(set(seq)) else list(range(max(seq)+1))
