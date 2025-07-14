def even_and_odd(n):
    e = ''.join(d for d in str(n) if int(d) % 2 == 0) or '0'
    o = ''.join(d for d in str(n) if int(d) % 2 == 1) or '0'
    return (int(e), int(o))
