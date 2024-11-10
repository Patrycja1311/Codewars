def time_correct(t):
    if not t or len(t) != 8 or t[2] != ':' or t[5] != ':':
        return t if t == "" else None

    try:
        h, m, s = map(int, t.split(":"))
        m += s // 60
        s %= 60
        h += m // 60
        m %= 60
        h %= 24
        return f"{h:02}:{m:02}:{s:02}"
    except ValueError:
        return None
