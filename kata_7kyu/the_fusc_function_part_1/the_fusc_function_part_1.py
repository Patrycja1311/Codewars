def fusc(n):
    return n if n < 2 else fusc(n // 2) + (fusc(n // 2 + 1) if n % 2 else 0)
