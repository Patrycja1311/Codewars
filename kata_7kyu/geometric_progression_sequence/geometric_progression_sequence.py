def geometric_sequence_elements(a, r, n):
    sequence = [a * (r ** i) for i in range(n)]
    return ', '.join(map(str, sequence))
