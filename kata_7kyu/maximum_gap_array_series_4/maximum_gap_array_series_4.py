def max_gap(numbers):
    numbers.sort()
    return max(numbers[i] - numbers[i-1] for i in range(1, len(numbers)))
