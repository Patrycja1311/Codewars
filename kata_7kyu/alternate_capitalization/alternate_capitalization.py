def capitalize(s):
    str_first = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    str_snd = str_first.swapcase()
    return [str_first, str_snd]
