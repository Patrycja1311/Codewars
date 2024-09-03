def sum_of_n(n):
    return [(i * (i + 1) // 2) * (1 if n >= 0 else -1) for i in range(abs(n) + 1)]
