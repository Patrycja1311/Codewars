def pyramid(s):
    if (s - 2) % 4 != 0:
        return None
    n = (s - 2) // 4
    V = n + 1
    E = 2 * n
    F = n + 1
    return V, E, F, n
