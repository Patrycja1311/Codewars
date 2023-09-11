def hamming_weight(x):
    binary_num = bin(x)[2:]
    return sum(int(n) for n in binary_num)
