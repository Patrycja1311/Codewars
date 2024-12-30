def calc(arr):
    return sum(
        x**2 * (-1 if (i + 1) % 5 == 0 else 1) * (3 if (i + 1) % 3 == 0 else 1)
        if x > 0 else x * (-1 if (i + 1) % 5 == 0 else 1) * (3 if (i + 1) % 3 == 0 else 1)
        for i, x in enumerate(arr)
    )
