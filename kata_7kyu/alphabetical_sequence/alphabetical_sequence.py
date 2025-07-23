def alpha_seq(strng):
    return ','.join(c.upper() + c.lower() * (ord(c.lower()) - 97) for c in sorted(strng, key=str.lower))
