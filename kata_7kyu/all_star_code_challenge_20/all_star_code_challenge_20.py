def add_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arrays must be of equal length")
    return [a + b for a, b in zip(array1, array2)]
