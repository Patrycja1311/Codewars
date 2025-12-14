def next_prime(n):
    def p(x):
        if x < 2 or x % 2 == 0 and x != 2: return False
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0: return False
        return True
    n += 1
    while not p(n): n += 1
    return n
