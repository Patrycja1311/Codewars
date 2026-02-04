def interweave(s1, s2):
    res = ''.join(a + b for a, b in zip(s1, s2)) + s1[len(s2):] + s2[len(s1):]
    return ''.join(c for c in res if not c.isdigit()).strip()
