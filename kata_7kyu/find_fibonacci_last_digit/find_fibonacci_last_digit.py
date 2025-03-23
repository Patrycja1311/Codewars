def get_last_digit(index):
    a, b = 0, 1
    for _ in range(index % 60):
        a, b = b, (a + b) % 10
    return a
