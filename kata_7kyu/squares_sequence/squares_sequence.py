def squares(x, n):
    return [x ** (2 ** i) for i in range(n)] if n > 0 else []
