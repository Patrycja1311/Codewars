def sum_triangular_numbers(n):
    if n < 1:
        return 0
    total_sum = 0
    for i in range(1, n + 1):
        triangular_number = i * (i + 1) // 2
        total_sum += triangular_number

    return total_sum
