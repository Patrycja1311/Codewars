def square_it(digits):
    s = str(digits)
    n = int(len(s) ** 0.5)
    return '\n'.join(s[i:i+n] for i in range(0, len(s), n)) if n*n == len(s) else 'Not a perfect square!'
