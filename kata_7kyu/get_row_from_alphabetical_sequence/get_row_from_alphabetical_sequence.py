def get_row(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = (n - 1) % 26 + 1
    return alphabet[n - 1] * n + alphabet[n:]
