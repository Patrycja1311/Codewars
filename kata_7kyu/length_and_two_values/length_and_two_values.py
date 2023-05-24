def alternate(n, first_value, second_value):
    results = []
    for i in range(n):
        if i % 2 == 0:
            results.append(first_value)
        else:
            results.append(second_value)
    return results
