def powers(n):
    return [2**i for i in range(n.bit_length()) if n & (1 << i)]