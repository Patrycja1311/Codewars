def count_bits(n):
    binary_sum = sum([int(x) for x in bin(n)[2:]])
    return binary_sum
