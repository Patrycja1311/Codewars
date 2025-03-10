def is_pronic(n):
    return any(i * (i + 1) == n for i in range(int(n**0.5) + 1)) if n >= 0 else False
