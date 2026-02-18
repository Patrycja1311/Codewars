def number_property(n):
    if n <= 1:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(abs(n)**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
    is_even = (n % 2 == 0)
    is_multiple_10 = (n % 10 == 0)
    return [is_prime, is_even, is_multiple_10]
