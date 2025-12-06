def red_knight(N, P):
    return ("White", 2*P) if (N + P) % 2 == 0 else ("Black", 2*P)
