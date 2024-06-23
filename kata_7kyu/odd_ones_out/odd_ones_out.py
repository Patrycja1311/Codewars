def odd_ones_out(numbers):
    from collections import Counter
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] % 2 == 0]