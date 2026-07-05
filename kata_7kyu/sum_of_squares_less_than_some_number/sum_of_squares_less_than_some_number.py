def get_number_of_squares(n):
    total = 0
    i = 1
    while total + i * i < n:
        total += i * i
        i += 1
    return i - 1
