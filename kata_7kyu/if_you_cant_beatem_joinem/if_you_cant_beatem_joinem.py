def cant_beat_so_join(numbers):
    sorted_numbers = sorted(numbers, key=sum, reverse=True)
    return [num for group in sorted_numbers for num in group]
