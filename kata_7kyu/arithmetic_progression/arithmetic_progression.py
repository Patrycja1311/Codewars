def arithmetic_sequence_elements(a, d, n):
    sequence = [str(a + d * i) for i in range(n)]
    return ', '.join(sequence)
