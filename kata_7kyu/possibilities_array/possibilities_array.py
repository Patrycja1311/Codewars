def is_all_possibilities(arr):
    n = len(arr)
    return sorted(arr) == list(range(n))
