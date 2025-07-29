def coin_combo(cents):
    q, cents = divmod(cents, 25)
    d, cents = divmod(cents, 10)
    n, p = divmod(cents, 5)
    return [p, n, d, q]
