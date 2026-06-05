def help_zoom(key):
    n = int(len(key) ** 0.5)
    if n*n != len(key): return "No"
    m = [key[i*n:(i+1)*n] for i in range(n)]
    return "Yes" if m == [r[::-1] for r in m[::-1]] else "No"

