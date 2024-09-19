def find_missing_number(sequence):
    try:
        numbers = sorted(map(int, sequence.split()))
    except ValueError:
        return 1
    for i, num in enumerate(numbers, 1):
        if num != i:
            return i
    return 0
