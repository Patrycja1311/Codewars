def encode(st):
    return ''.join(str(ord(c.lower()) - 96) if c.isalpha() else c for c in st)
