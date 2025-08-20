def count_consonants(text):
    return len({c.lower() for c in text if c.isalpha() and c.lower() not in "aeiou"})
