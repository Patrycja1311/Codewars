def heggeleggleggo(word):
    return ''.join(c + 'egg' if c.lower() not in 'aeiou ' else c for c in word)
