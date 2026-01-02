def title_to_number(title):
    return sum((ord(c) - 64) * 26 ** i for i, c in enumerate(reversed(title)))
