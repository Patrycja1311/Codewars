def is_divisible(n, *divisors):
    return all(n % d == 0 for d in divisors)
