def check_three_and_two(array):
    counts = set(array)
    return len(counts) == 2 and array.count(counts.pop()) in [2, 3]
