def binary_pyramid(m, n):
    total = sum(int(bin(i)[2:]) for i in range(m, n + 1))
    return bin(total)[2:]
