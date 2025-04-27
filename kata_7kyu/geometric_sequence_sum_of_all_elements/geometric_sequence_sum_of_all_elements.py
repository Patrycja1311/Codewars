def geometric_sequence_sum(a, r, n):
    return a * (1 - r**n) / (1 - r) if r != 1 else a * n
