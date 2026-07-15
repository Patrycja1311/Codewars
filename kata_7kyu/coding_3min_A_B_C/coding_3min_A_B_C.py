def find_a_b(numbers, c):
    for i, a in enumerate(numbers):
        for b in numbers[i + (a == numbers[i]):]:
            if a * b == c:
                return [a, b]
    return None

