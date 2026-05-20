def int_rac(n, guess):
    c = 0
    while True:
        c += 1
        nxt = (guess + n // guess) // 2
        if nxt == guess:
            return c
        guess = nxt
