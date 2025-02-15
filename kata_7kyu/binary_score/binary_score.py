def score(n):
    return (1 << n.bit_length()) - 1 if n else 0
