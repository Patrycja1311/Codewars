def layers(n):
    k = 1
    while (2 * k - 1) ** 2 < n:
        k += 1
    return k
