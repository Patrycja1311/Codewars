def lottery(s):
    res = []
    return ''.join([res.append(c) or c for c in s if c.isdigit() and c not in res]) or "One more run!"
