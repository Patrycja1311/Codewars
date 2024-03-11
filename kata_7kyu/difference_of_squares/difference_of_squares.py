def difference_of_squares(n):
    sum_of_numbers = n * (n + 1) // 2
    square_of_sum = sum_of_numbers ** 2
    sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
    return square_of_sum - sum_of_squares
