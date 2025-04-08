def perfect_roots(n):
    if n <= 1:
        return False
    r2 = n ** (1/2)
    r4 = n ** (1/4)
    r8 = n ** (1/8)
    return r2.is_integer() and r4.is_integer() and r8.is_integer()
