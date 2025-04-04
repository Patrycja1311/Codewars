def climb(n):
    sequence = []
    while n > 0:
        sequence.append(n)
        n //= 2
    return sequence[::-1]
