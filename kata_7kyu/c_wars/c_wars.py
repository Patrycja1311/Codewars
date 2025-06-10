def initials(name):
    *rest, last = name.split()
    return ''.join(f'{w[0].upper()}.' for w in rest) + last.capitalize()
