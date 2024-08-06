def minimum_steps(numbers, value):
    numbers.sort()
    total = 0
    for i, num in enumerate(numbers):
        total += num
        if total >= value:
            return i
