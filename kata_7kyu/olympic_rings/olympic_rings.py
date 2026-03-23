def olympic_ring(string):
    s = sum(2 if c == 'B' else 1 if c in 'abdegopqADOPRQ' else 0 for c in string) // 2
    return ['Not even a medal!', 'Not even a medal!', 'Bronze!', 'Silver!', 'Gold!'][min(s, 4)]
