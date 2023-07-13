def series_sum(n):
    return format(sum((1 / (1 + i * 3)) for i in range(n)), ".2f")
