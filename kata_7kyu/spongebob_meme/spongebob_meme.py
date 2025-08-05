def sponge_meme( s ):
    i = 0
    return ''.join(c.upper() if (i := i+1) % 2 else c.lower() if c.isalpha() else c for c in s if not c.isalpha() or True)
