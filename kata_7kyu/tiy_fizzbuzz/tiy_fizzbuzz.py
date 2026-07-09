def tiy_fizz_buzz(string):
    return "".join(
        "Iron Yard" if c in "AEIOU" else
        "Iron" if c in "BCDFGHJKLMNPQRSTVWXYZ" else
        "Yard" if c in "aeiou" else c
        for c in string
    )
