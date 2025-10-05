def remove(text, what):
    c = dict(what)
    return ''.join(ch for ch in text if c.get(ch, 0) == 0 or (c.update({ch:c[ch]-1}), False)[1])
