def solve(a, b):
    return a == b if '*' not in a else b.startswith(a.split('*')[0]) and b.endswith(a.split('*')[1]) and len(b) >= len(a) - 1
