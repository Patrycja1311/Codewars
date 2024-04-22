def number_joy(n):
    s = sum(int(d) for d in str(n))
    return n % s == 0 and int(str(s)[::-1]) * s == n
