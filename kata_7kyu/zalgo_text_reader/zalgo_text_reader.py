def read_zalgo(zalgotext):
    return ''.join(c for c in zalgotext if ord(c) < 128)
