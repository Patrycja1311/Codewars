def solve(s, g):
    return tuple([g, s - g]) if s % g == 0 else -1
