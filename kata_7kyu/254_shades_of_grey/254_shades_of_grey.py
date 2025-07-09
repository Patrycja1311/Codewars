def shades_of_grey(n):
    n = max(0, min(n, 254))
    return [f"#{i:02x}{i:02x}{i:02x}" for i in range(1, n + 1)]

