def per(n):
    r = []
    while n > 9:
        p = 1
        for x in str(n):
            p *= int(x)
        r.append(p)
        n = p
    return r
