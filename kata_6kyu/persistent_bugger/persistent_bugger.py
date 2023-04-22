def persistence(n):
    count_iteration = 0
    while len(str(n)) > 1:
        result = 1
        for digit in str(n):
            result *= int(digit)
        count_iteration += 1
        n = result
    return count_iteration
