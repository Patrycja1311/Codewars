def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(n, i - 1, -1)) for i in range(1, n + 1)) if n > 0 else ''
