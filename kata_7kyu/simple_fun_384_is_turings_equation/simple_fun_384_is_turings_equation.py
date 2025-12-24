def is_turing_equation(s):
    a, b = s.split('=')
    x, y = a.split('+')
    return int(x[::-1]) + int(y[::-1]) == int(b[::-1])
