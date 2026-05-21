def battle(x: str, y: str) -> str:
    s = lambda w: sum((ord(c) - 96) / 2 if c.islower() else ord(c) - 64 for c in w)
    a, b = s(x), s(y)
    return x if a > b else y if b > a else "Tie!"
