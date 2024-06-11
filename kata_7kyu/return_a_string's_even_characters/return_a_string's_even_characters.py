def even_chars(st):
    return "invalid string" if len(st) < 2 or len(st) > 100 else [st[i] for i in range(1, len(st), 2)]
