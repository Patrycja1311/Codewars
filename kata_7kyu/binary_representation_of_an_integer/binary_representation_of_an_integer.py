def show_bits(n):
    n = n & 0xFFFFFFFF
    return [(n >> i) & 1 for i in range(31, -1, -1)]
