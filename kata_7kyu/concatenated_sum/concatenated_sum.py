def check_concatenated_sum(n, t):
    if t == 0:
        return False
    s = str(abs(n))
    return n == sum(int(d * t) for d in s) * (1 if n >= 0 else -1)
