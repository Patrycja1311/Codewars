def grid(N):
    if N < 0: return None
    return '\n'.join(' '.join(chr((i + j) % 26 + 97) for j in range(N)) for i in range(N))
