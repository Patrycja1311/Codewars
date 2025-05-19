def alternate_sq_sum(arr):
    return sum(x**2 if i % 2 else x for i, x in enumerate(arr))
