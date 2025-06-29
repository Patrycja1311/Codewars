def equable_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a: return False
    s = (a + b + c) / 2
    return abs((s*(s - a)*(s - b)*(s - c))**0.5 - (a + b + c)) < 1e-6
