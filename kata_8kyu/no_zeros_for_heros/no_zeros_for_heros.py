def no_boring_zeros(n):
    return int(str(n).rstrip('0')) if n > 0 or n < 0 else 0
