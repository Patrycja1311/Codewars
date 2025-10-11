def hex_hash(code):
    return sum(int(ch) for c in code for ch in hex(ord(c))[2:] if ch.isdigit())
