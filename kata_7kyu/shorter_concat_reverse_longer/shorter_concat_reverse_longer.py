def shorter_reverse_longer(a, b):
    a, b = a or "", b or ""
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a
