def is_valid(idn):
    if not idn:
        return False
    return (idn[0].isalpha() or idn[0] in '_$') and \
           all(c.isalnum() or c in '_$' for c in idn)
