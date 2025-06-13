def calculate(n1, n2, o):
    ops = {'add': int.__add__, 'subtract': int.__sub__, 'multiply': int.__mul__}
    to_int = lambda x: -int(x[1:], 2) if x.startswith('-') else int(x, 2)
    res = ops[o](to_int(n1), to_int(n2))
    return '-' + bin(-res)[2:] if res < 0 else bin(res)[2:]
