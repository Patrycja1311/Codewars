def trim(phrase, size):
    if size <= 3:
        return (phrase[:size] + '...') if len(phrase) > size else phrase
    if len(phrase) <= size:
        return phrase
    return phrase[:size - 3] + '...'
