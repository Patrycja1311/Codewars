def even_last(numbers):
    return sum(numbers[i] for i in range(0, len(numbers), 2)) * numbers[-1] if numbers else 0
