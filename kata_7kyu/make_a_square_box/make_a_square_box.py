def box(n):
    return ['-' * n] + ['-' + ' ' * (n - 2) + '-' for _ in range(n - 2)] + ['-' * n]
