def validate_sequence(sequence):
    d = sequence[1] - sequence[0]
    return all(sequence[i] - sequence[i-1] == d for i in range(2, len(sequence)))
