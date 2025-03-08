def max_product(a):
    max1, max2 = 0, 0
    for n in a:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
    return max1 * max2
