def word_pattern(word):
    word = word.lower()
    seen = {}
    return '.'.join(str(seen.setdefault(c, len(seen))) for c in word)
