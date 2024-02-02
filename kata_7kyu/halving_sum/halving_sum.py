def halving_sum(n):
    return n + sum(n // (2**i) for i in range(1, n.bit_length()))
