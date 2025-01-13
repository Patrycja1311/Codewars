def binary_cleaner(seq):
    less_than_two = [x for x in seq if x < 2]
    indices_greater_than_one = [i for i, x in enumerate(seq) if x > 1]
    return (less_than_two, indices_greater_than_one)
