def generate_pairs(m, n):
    return [(a, b) for a in range(m, n + 1) for b in range(a, n + 1)]
