def re_ordering(text):
    words = text.split()
    capital_word = next(word for word in words if word[0].isupper())
    return " ".join([capital_word] + [w for w in words if w != capital_word])
