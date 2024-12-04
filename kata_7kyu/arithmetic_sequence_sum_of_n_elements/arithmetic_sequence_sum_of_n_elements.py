def arithmetic_sequence_sum(a, r, n):
    total_sum = 0
    current_value = a
    for i in range(n):
        total_sum += current_value
        current_value += r
    return total_sum
