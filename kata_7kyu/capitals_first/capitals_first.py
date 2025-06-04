def capitals_first(text):
    words = text.split()
    up = [w for w in words if w[0].isupper()]
    low = [w for w in words if w[0].islower()]
    return ' '.join(up + low)
