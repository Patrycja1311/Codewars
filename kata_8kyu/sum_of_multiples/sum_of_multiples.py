def sum_mul(n, m):
    if n > 0 and m > 0:
        numbers = [x for x in range(n, m) if x % n == 0]
        return sum(numbers)
    else:
        return 'INVALID'
